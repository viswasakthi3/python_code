
import requests
import json
from flask import Flask, redirect,render_template,request
app = Flask(__name__)

app.route('/')
def hey():
    response = requests.get('http://127.0.0.1:4999/store')
    return response.json()

app.run()