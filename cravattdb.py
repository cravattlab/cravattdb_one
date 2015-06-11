from flask import Flask, request, render_template, json
from werkzeug import FileStorage
from models.upload import Experiment, Experiments
from models.list import List
from models.dataset import Dataset
from models.uploadRaw import UploadRaw
import config

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['PROPAGATE_EXCEPTIONS'] = True # don't swallow error messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods = [ 'POST' ])
def upload():
    file = request.files['file']
    experiment_id = request.form.get('experimentId')

    if file.filename and isinstance(file, FileStorage) and experiment_id:
        Experiment().upload_file(file, experiment_id)
        return 'hi'

@app.route('/new', methods=['GET', 'POST'])
@app.route('/new/<int:experiment_id>', methods=['GET', 'POST'])
def new(experiment_id=None):
    if request.method == 'GET':
        return render_template('index.html', bootstrap = json.dumps(Experiments().bootstrap()))
    else:
        if not experiment_id:
            experiment = Experiment()
            new_id = experiment.new(request.json)
            return json.dumps({ 'success': new_id })

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

@app.route('/api/experiment/<int:experiment_id>')
def experiment_api(experiment_id):
    return json.dumps(Experiment().fetch(experiment_id))

@app.route('/api/dataset/<int:experiment_id>')
def dataset_api(experiment_id):
    return json.dumps(Dataset(experiment_id).bootstrap())

@app.route('/api/new', methods=['GET'])
def new_api():
    return json.dumps(Experiments().bootstrap())

@app.route('/test')
def test():
    return('<img src="file:///localhost/c:/Users/Radu/Desktop/wp_ss_20130927_0001.png" width="100px" height="100px" />') 

if __name__ == "__main__":
    app.run(host='0.0.0.0')