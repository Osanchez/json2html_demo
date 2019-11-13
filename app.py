from flask import Flask, request
from flask import render_template
from json2html import *

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        try:
            json_text = request.form['json']
            converted_text = json2html.convert(json=json_text)

            if '<table' not in converted_text:
                raise Exception

        except Exception:
            converted_text = '<h2>Could not convert JSON object</h2><h3>Please check JSON syntax</h3>'

        return converted_text
    else:
        return render_template('json2html.html')


if __name__ == '__main__':
    app.run(debug=True)
