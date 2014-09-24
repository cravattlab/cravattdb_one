from db.db import Database
from uploadForm import UploadForm
from string import Template
from csv import reader

class Experiment:
    def __init__(self, file, form):
        self.__file = file
        self.__form = form
        self.__db = Database()

    def process(self):
        # first we validate the form submission
        form = UploadForm(self.__form)

        # if not form.validate():
        #     # do something if form is not valid
        #     print 'Form was not valid'

        form.validate()

        # then we get a name for our experiment
        name = self.__get_experiment_name()

        # and insert the experimental data
        self.__insert_data(name)
        self.__insert_experiment(name)


    def __insert_experiment(self, name):
        '''
            INSERT INTO experiments (user_id, experiment_type, sample_type, organism_id, cell_line, probe_id, inhibitor_id, name, description)
            VALUES (
                form.username,
                form.experiment_type,
                form.sample_type,
                form.organism,
                form.cell_line
                form.probe,
                form.inhibitor,
                form.name,
                form.description
            )


        '''

        return True

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

        self.__db.connection.commit()
        self.__db.close()

    def __get_experiment_name(self):
        # temporary name for testing
        # need to establish a naming scheme for future
        return 'test'