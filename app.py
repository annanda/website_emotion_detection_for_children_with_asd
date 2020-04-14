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


@app.route('/about_project', methods=['GET'])
def project_page():
    return render_template('project.html')


@app.route('/contact', methods=['GET'])
def contact_page():
    return render_template('contact.html')


@app.route('/data_protection_ethics', methods=['GET'])
def ethics_page():
    return render_template('data_protection_ethics.html')


@app.route('/researchers', methods=['GET'])
def researchers_page():
    return render_template('researchers.html')


@app.route('/information', methods=['GET'])
def information_page():
    return render_template('documents.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9090)
