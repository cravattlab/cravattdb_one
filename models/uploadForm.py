from wtforms import Form, BooleanField, TextField, SelectField, PasswordField, validators

class UploadForm(Form)
    organism = SelectField('Organism', [InputRequired(), check_against_db()])
    sample_type = SelectField('Sample Type', [InputRequired(), check_against_db ()])
    experiment_type = SelectField('Experiment Type', [InputRequired(), check_against_db()])
    cell_line = SelectField('Cell Line', [Optional(), check_against_db()])
    inhibitor = SelectField('Inhibitor', [Optional(), check_against_db()])
    probe = SelectField('Probe', [Optional(), check_against_db()])
    username = TextField('Username', [InputRequired(), check_against_db()])
    dataset_name = TextField('Dataset Name', [InputRequired()])
    description = TextAreaField('Decription', [InputRequired()])

    def check_against_db(name):
    entry = field.data

    message = '%s not found in %s database' % (name, entry)

    def _check_db(form, field):
        return db.cursor.execute(Template(
            'SELECT EXISTS(SELECT 1 FROM $table WHERE id = %(entry)s)'
        ).substitute(table = name), { 'entry': entry })

    return _check_db