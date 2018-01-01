from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import uuid
import argparse

# Check if being run on dev (production by default)
parser = argparse.ArgumentParser()
parser.add_argument('-dev', action='store_true', dest='dev', help='Runs program with dev settings')
args = parser.parse_args()

app = Flask(__name__)

DEV = args.dev


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/upload_data', methods=['POST'])
def upload_data():
    if request.method == 'POST':

        # TODO: Null checks for these files and see if they're the right type of files
        data_file = request.files['data']
        labels_file = request.files['labels']

        # give unique filenames for data and labels
        data_filename = secure_filename(str(uuid.uuid4()) + '.txt')
        labels_filename = secure_filename(str(uuid.uuid4()) + '.txt')

        # import ipdb;
        # ipdb.set_trace()

        upload_address = '/var/www/MADA/uploads'

        if DEV:
            upload_address = '/Users/sujeethjinesh/Desktop/MADA/uploads/'

        data_address = upload_address + data_filename
        labels_address = upload_address + labels_filename

        data_file.save(data_address)
        labels_file.save(labels_address)

    return "it works!!!"


if __name__ == '__main__':
    app.run(debug=True)
