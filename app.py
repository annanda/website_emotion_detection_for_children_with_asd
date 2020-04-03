from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder="./templates")


@app.route('/', methods=['GET'])
def index():
    info = {}
    return "Hello World"
    # return render_template('index.html', **info)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9090)
