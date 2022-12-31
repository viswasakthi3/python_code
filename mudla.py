from contextlib import nullcontext
from typing import List
import requests
import json
from flask import Flask,render_template,request




app = Flask(__name__)

@app.route('/')
@app.route('/search')
def homepage():
    return render_template('search.html')

@app.route('/show',methods=['POST','GET'])
def abc():
    if request.method =='post':
        n=request.form.post('quantity')
        render_template('show.html',quantity=n) 