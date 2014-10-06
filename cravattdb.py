from flask import Flask, request, render_template, json
from werkzeug import FileStorage
from models.upload import Experiment, Experiments

app = Flask(__name__)
app.config.from_object(__name__)
DEBUG = True
# add this so that flask doesn't swallow error messages
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods = ['GET', 'POST'])
def add():
    if request.method == 'GET':
        experiments = Experiments()
        return render_template('index.html', bootstrap = json.dumps(experiments.bootstrap()))
    else:
        file = request.files['file']

        # Validate that what we have been supplied with is infact a file
        if file.filename and isinstance(file, FileStorage):
            experiment = Experiment(file, request.form)
            status = experiment.process()

            file.close()

        return ''

if __name__ == "__main__":
    app.run()