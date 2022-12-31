

from contextlib import nullcontext
from typing import List
import requests
import json
from flask import Flask, redirect,render_template,request, url_for




app = Flask(__name__)


response = requests.get('https://f8776af4-e760-4c93-97b8-70015f0e00b3.mock.pstmn.io/fruits')


@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/')
def n():
    for data in (response.json()):
        if data['name'] == "orange":
            print(data['name'])


if __name__ == "__main__":
    app.run(debug=True)