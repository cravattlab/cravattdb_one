from flask import Flask, request, render_template, json
from werkzeug import FileStorage
from models.upload import Experiment, Experiments
from models.list import List
from models.dataset import Dataset
from models.uploadRaw import UploadRaw

app = Flask(__name__)
app.config.from_object(__name__)
app.debug = True
DEBUG = True
# add this so that flask doesn't swallow error messages
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods = [ 'POST' ])
def upload():
    file = request.files['file']
    uploader = UploadRaw(file)
    uploader.move()
    return 'hi'

@app.route('/add', methods = ['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('index.html', bootstrap = json.dumps(Experiments().bootstrap()))
    else:
        file = request.files['file']

        # Validate that what we have been supplied with is infact a file
        if file.filename and isinstance(file, FileStorage):
            experiment = Experiment(file, request.form)
            status = experiment.process()

            file.close()

        return ''

@app.route('/list')
def list():
    return render_template('index.html', bootstrap = json.dumps(List().bootstrap()))

@app.route('/api/list')
def list_api():
    return json.dumps(List().bootstrap())

@app.route('/dataset/<int:experiment_id>')
def dataset(experiment_id):
    dataset = Dataset(experiment_id)

    return render_template(
        'index.html',
        bootstrap = json.dumps(dataset.bootstrap())
    )

@app.route('/api/dataset/<int:experiment_id>')
def dataset_api(experiment_id):
    return json.dumps(Dataset(experiment_id).bootstrap())

@app.route('/api/add', methods=['GET'])
def add_api():
    return json.dumps(Experiments().bootstrap())

@app.route('/test')
def test():
    return('<img src="file:///localhost/c:/Users/Radu/Desktop/wp_ss_20130927_0001.png" width="100px" height="100px" />') 

if __name__ == "__main__":
    app.run(host='0.0.0.0')
