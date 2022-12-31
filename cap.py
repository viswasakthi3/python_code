
from flask import Flask, jsonify

app = Flask(__name__)
stores = [{"name": "Apple", "qty": 10 }, { "name": "Mango", "qty": 8 }, { "name": "Orange", "qty": 6 } ]
print(stores)

