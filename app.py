from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/upload_data', methods=['POST'])
def upload_data():
    if request.method == 'POST':
        import ipdb;
        ipdb.set_trace()

        #TODO: make sure to use request.files['data']. Currently not in right format.
        data_labels_dict = request.get_json()
        data = data_labels_dict['data'][0]['preview']
        labels = data_labels_dict['labels'][0]['preview']

        # data.save('/var/www/uploads/uploaded_file.txt')
    return "it works"


if __name__ == '__main__':
    app.run(debug=True)
