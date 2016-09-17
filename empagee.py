from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('login.html')

@app.route("/home")
def home():
	return render_template('home.html')

@app.route("/patients")
def patients():
	return render_template('patients.html')

@app.route("/patient1")
def patient1():
	return render_template('patient1.html')

@app.route("/signup")
def signup():
	return render_template('signup.html')

@app.route("/takePhoto")
def takePhoto():
	return render_template('takePhoto.html')

@app.route("/analysis")
def analysis():
	return render_template('analysis.html')

@app.route("/analyseExpression")
def analyseExpression():
	return render_template('analyseExpression.html')


if __name__ == "__main__":
    app.run()
