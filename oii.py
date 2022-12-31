from contextlib import nullcontext
from typing import List
from urllib import response
import requests
import json
from flask import Flask, redirect,render_template,request
app = Flask(__name__)


response0 = [{"name": "Apple", "qty": 10 }, { "name": "Mango", "qty": 8 }, { "name": "Orange", "qty": 6 } ]
response2 = [{"name": "rice", "qty": 10 }, { "name": "wheat", "qty": 8 }, { "name": "dhal", "qty": 6 } ]
response3 = [{"name": "carrot", "qty": 10 }, { "name": "beetroot", "qty": 8 }, { "name": "onion", "qty": 6 } ]

@app.route('/')
def homepage():
    return render_template('search.html')

@app.route('/show',methods=['POST','GET'])
def abc():
    #response = requests.get('https://f8776af4-e760-4c93-97b8-70015f0e00b3.mock.pstmn.io/fruits')
    #response2 = requests.get('https://f8776af4-e760-4c93-97b8-70015f0e00b3.mock.pstmn.io/vegetables')
    #response3 = requests.get('https://f8776af4-e760-4c93-97b8-70015f0e00b3.mock.pstmn.io/grains')
    if request.method =="POST":
        n = request.form["quantity"]
        lis=[]
        for data in (response0):
            if data['qty'] >= int(n):
                lis.append(data['name'])

        for data in (response2):
            if data['qty'] >= int(n):
                lis.append(data['name'])

        for data in (response3):
            if data['qty'] >= int(n):
                lis.append(data['name']) 
                lis.sort()
    if lis!=[]:
        pass
    else:
        lis="not found"


    return render_template("show.html",variable=lis)

if __name__ == "__main__":
    app.run(debug=True)



    
