from flask import Flask, render_template, request, send_file
from config import PGSQL_DATABASE_NAME, PGSQL_DATABASE_USER, PGSQL_DATABASE_PASSWORD
from werkzeug import secure_filename, FileStorage
import os, psycopg2, csv

app = Flask(__name__)
app.config.from_object(__name__)
DEBUG = True
# add this so that flask doesn't swallow error messages
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return send_file('templates/index.html')
    else:
        file = request.files['file']
        if file.filename:
            # Validate that what we have been supplied with is infact a file
            if not isinstance(file, FileStorage):
                raise TypeError("storage must be a werkzeug.FileStorage")

            insert_data(file)
            file.close()

        return ''

def insert_data(file):
    conn = psycopg2.connect(
        database = PGSQL_DATABASE_NAME,
        user = PGSQL_DATABASE_USER,
        password = PGSQL_DATABASE_PASSWORD
    )

    cur = conn.cursor()

    # temporary name for testing
    # need to establish a naming scheme for future
    name = file.filename

    # create table that we're going to insert into
    with open('db/schema/templates/experiment-child.sql') as table_template:
        create_sql = Template(table_template.read()).substitute(table = name)

    cur.execute(create_sql)

    insert_sql = Template(
        'INSERT INTO $table (peptide_index, ipi, description, symbol, '
            'sequence, mass, charge, segment, ratio, intensity, num_ms2_peaks,'
            'num_candidate_peaks, max_light_intensity, light_noise,'
            'max_heavy_intensity, heavy_noise, rsquared, entry, link) '
        'VALUES (%(peptide_index)s, %(ipi)s, %(description)s, %(symbol)s,'
            '%(sequence)s, %(mass)s, %(charge)s, %(segment)s, %(ratio)s, %(intensity)s, %(num_ms2_peaks)s,'
            '%(num_candidate_peaks)s, %(max_light_intensity)s, %(light_noise)s,'
            '%(max_heavy_intensity)s, %(heavy_noise)s, %(rsquared)s, %(entry)s, %(link)s)'
    ).substitute(table=name)

    tsv = io.StringIO(file.read())

    for line in csv.reader(tsv, delimiter = '\t'):
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

        cur.execute(insert_sql, values)

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    app.run()