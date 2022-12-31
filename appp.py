from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "hey"


app.run(port=4888)    