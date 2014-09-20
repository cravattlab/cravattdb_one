from flask import Flask, request, send_file
from werkzeug import FileStorage
from upload import Experiment

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

        # Validate that what we have been supplied with is infact a file
        if file.filename && isinstance(file, FileStorage):
            experiment = Experiment(file, request.form)
            status = experiment.process()

            file.close()

        return ''

if __name__ == "__main__":
    app.run()