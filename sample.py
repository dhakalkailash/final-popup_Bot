from flask import Flask,render_template,request
app=Flask(__name__)  #create the object name with app

@app.route("/index")
@app.route("/")
def index():
	return render_template("index.html")

if __name__=='__main__':
	app.run(debug=True)

