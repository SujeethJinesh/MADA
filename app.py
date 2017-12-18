from flask import Flask, render_template
import os

template_dir = os.path.abspath('front_end/src/')
app = Flask(__name__, template_folder=template_dir)


@app.route('/')
def index():
    return render_template('templates/index.html')


@app.route('/hello')
def hello():
    return render_template('templates/hello.html')


if __name__ == '__main__':
    app.run(debug=True)
