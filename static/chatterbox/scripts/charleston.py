#! usr/bin/env python3

from flask import Flask, url_for, render_template, redirect
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


#url_for('static', filename='obble.css')

@app.route('/')
@cross_origin()
def index():
    return render_template('index.html')






if __name__ == '__main__':
    app.run(debug=True)



