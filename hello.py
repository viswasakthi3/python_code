from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
@app.route('/search')
def homepage():
    return render_template('search.html')

@app.route("/show",methods=['POST','GET'])
def search():
    if request.method =='POST':
        n=request.form.get('quantity')
        return render_template('show.html',quantity=n)


if __name__ == "__main__":
    app.run(debug=True)

