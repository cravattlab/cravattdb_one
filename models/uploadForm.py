from wtforms import Form, BooleanField, TextField, TextAreaField, SelectField, PasswordField, validators

def check_against_db():
    message = 'Parameter not found in database'

    def _check_db(form, field):
        return db.cursor.execute(Template(
            'SELECT EXISTS(SELECT 1 FROM $table WHERE id = %(field.data)s)'
        ).substitute(table = field.label), { 'entry': field.data })

    return _check_db

class UploadForm(Form):
    organism = SelectField('organism',  [validators.InputRequired(), check_against_db()])
    sample_type = SelectField('sample_types', [validators.InputRequired(), check_against_db ()])
    experiment_type = SelectField('experiment_typea', [validators.InputRequired(), check_against_db()])
    cell_line = SelectField('cell_lines', [validators.Optional(), check_against_db()])
    inhibitor = SelectField('inhibitors', [validators.Optional(), check_against_db()])
    probe = SelectField('probes', [validators.Optional(), check_against_db()])
    username = TextField('users', [validators.InputRequired(), check_against_db()])
    dataset_name = TextField('Dataset Name', [validators.InputRequired()])
    description = TextAreaField('Decription', [validators.InputRequired()])