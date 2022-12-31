from flask import Flask,render_template,request

asf = Flask(__name__)

@asf.route('/')
@asf.route('/search')
def homepage():
    return "hello"