from flask import Flask, render_template, request, url_for, redirect
from werkzeug.utils import secure_filename
import uuid
import argparse
import boto3

# Check if being run on dev (production by default)
parser = argparse.ArgumentParser()
parser.add_argument('-dev', action='store_true', dest='dev', help='Runs program with dev settings')
args = parser.parse_args()

app = Flask(__name__)

DEV = args.dev

s3 = boto3.resource('s3')

BUCKET_NAME = 'mada-bucket'

if DEV:
    app.debug = True


@app.route('/')
def main():
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

        upload_address = '/var/www/MADA/uploads'

        if DEV:
            upload_address = '/Users/sujeethjinesh/Desktop/MADA/uploads/'

        data_address = upload_address + data_filename
        labels_address = upload_address + labels_filename

        data_file.save(data_address)
        labels_file.save(labels_address)

        s3.meta.client.upload_file(data_address, BUCKET_NAME, data_filename)

        analysis(data_filename, labels_filename)

        return redirect(url_for('processed_data'))

    return "Houston, we have a problem."


# TODO: fix this and make it not a hardcoded url
@app.route('/processed_data')
def processed_data():
    return render_template('processed_data.html')


def analysis(data_filename, labels_filename):
    # pre_process_data(data_filename)
    pass


if __name__ == '__main__':
    app.run(debug=True)
