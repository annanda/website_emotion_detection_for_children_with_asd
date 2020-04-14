from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder="./templates")


@app.route('/', methods=['GET'])
def index():
    info = {}
    return render_template('index.html', **info)


@app.route('/index', methods=['GET'])
def index_page():
    info = {}
    return render_template('index.html', **info)


@app.route('/generic', methods=['GET'])
def generic_page():
    return render_template('generic.html')


@app.route('/elements', methods=['GET'])
def elements_page():
    return render_template('elements.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9090)
