from db.db import Database
from uploadForm import UploadForm
from string import Template
from csv import reader
from inflection import camelize, singularize, titleize

class Experiments:
    def __init__(self):
        self.__db = Database()

    def bootstrap(self):
        data = self.fetch_all();

        results = {}

        for item in data:
            results[camelize(item, False)] = {
                'label' : singularize(titleize(item)),
                'data': data[item],
                'name': singularize(item.lower())
            }

        return {
            'add': results
        }

    def fetch_all(self):
        tables = [
            'cell_lines',
            'sample_types',
            'experiment_types',
            'inhibitors',
            'organisms',
            'probes',
            'users'
        ]

        results = {}

        for table in tables:
            sql = 'SELECT * FROM {0}'.format(table)
            self.__db.dict_cursor.execute(sql)
            results[table] = self.__db.dict_cursor.fetchall()

        self.__db.connection.commit()
        self.__db.close()

        return results

class Experiment:
    def __init__(self, experiment_file, form):
        self.__file = experiment_file
        self.__form = form
        self.__db = Database()

    def process(self):
        # first we validate the form submission
        form = UploadForm(self.__form)

        # if not form.validate():
        #     # do something if form is not valid
        #     print 'Form was not valid'

        # form.validate()       

        id = self.__insert_experiment()

        # then we get a name for our experiment
        name = self.__get_experiment_name(id)

        # and insert the experimental data
        self.__insert_data(name)

        self.__db.connection.commit()
        self.__db.close()


    def __insert_experiment(self):
        with open('db/templates/experiments-insert.sql') as insert_template:
            insert_sql = insert_template.read()

        form = self.__form

        values = {
            'username' : form['user'],
            'experiment_type' : form['experiment_type'],
            'sample_type' : form['sample_type'],
            'organism' : form['organism'],
            'cell_line' : form['cell_line'],
            'probe' : form['probe'],
            'inhibitor' : form['inhibitor'],
            'name' : form['name'],
            'description' : form['description']
        }

        self.__db.cursor.execute(insert_sql, values)
        return self.__db.cursor.fetchone()[0]

    def __insert_data(self, name):
        # create table that we're going to insert into
        with open('db/templates/experiment-child.sql') as table_template:
            create_sql = Template(table_template.read()).substitute(table = name)

        self.__db.cursor.execute(create_sql)

        with open('db/templates/experiment-insert.sql') as insert_template:
            insert_sql = Template(insert_template.read()).substitute(table = name)

        isFirstLine = True;

        for line in reader(self.__file, delimiter = '\t'):
            if (isFirstLine): isFirstLine = False; continue

            values = {
                'peptide_index': line[0],
                'ipi': line[1],
                'description': line[2],
                'symbol': line[3],
                'sequence': line[4],
                'mass': line[5],
                'charge': line[6],
                'segment': line[7],
                'ratio': line[8],
                'intensity': line[9],
                'num_ms2_peaks': line[10].split('/')[0],
                'num_candidate_peaks': line[10].split('/')[1],
                'max_light_intensity': line[10].split('/')[2],
                'light_noise': line[10].split('/')[3],
                'max_heavy_intensity': line[10].split('/')[4],
                'heavy_noise': line[10].split('/')[5],
                'rsquared': line[11],
                'entry': line[12],
                'link': line[13]
            }

            self.__db.cursor.execute(insert_sql, values)

    def __get_experiment_name(self, id):
        return 'experiment_' + str(id)