from flask import Flask,render_template,request

asf = Flask(__name__)

@asf.route('/')
@asf.route('/search')
def homepage():
    return render_template('search.html')

asf.route("/show",methods=['POST','GET'])
def search():
    if request.method =='POST':
        n=request.form.get('name')
        return render_template('show.html',name=n)


if __name__ == "__main__":
    asf.run(debug=True)

