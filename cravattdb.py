from flask import Flask, render_template, request, send_file
from werkzeug import secure_filename, FileStorage
import os

app = Flask(__name__)

# see http://stackoverflow.com/questions/15981637/flask-how-to-handle-application-octet-stream
# for some hints
app.config.from_object(__name__)
DEBUG = True
# add this so that flask doesn't swallow error messages
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return send_file('templates/index.html')
    else:
        print request.file
        return 'nice bro nice'

if __name__ == "__main__":
    app.run()