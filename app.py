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

        data = request.files['data']
        labels = request.files['labels']

        # TODO: update this for dev server
        data.save('/Users/sujeethjinesh/Desktop/data1.txt')
        labels.save('/Users/sujeethjinesh/Desktop/labels1.txt')

    return "it works"


if __name__ == '__main__':
    app.run(debug=True)
