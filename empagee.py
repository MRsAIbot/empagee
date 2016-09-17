from flask import Flask
from flask import render_template, request, redirect, url_for, send_from_directory, json
from werkzeug.utils import secure_filename

import os
import base64
import json

app = Flask(__name__)

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'uploads/')
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

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


# Route that will process the file upload
@app.route('/upload', methods = ['POST'])
def upload():
	if request.headers['Content-Type'] == 'text/html':

		imgstr = request.data
		output = open('uploads/output.png', 'wb')

		output.write(imgstr.decode('base64'))

		output.close()
		return "JSON Message: " + request.data
	    # # Get the name of the uploaded file
	    # file = request.files['file']
	    # # Check if the file is one of the allowed types/extensions
	    # if file and allowed_file(file.filename):
	    #     # Make the filename safe, remove unsupported chars
	    #     filename = secure_filename(file.filename)
	    #     # Move the file form the temporal folder to
	    #     # the upload folder we setup
	    #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	    #     # Redirect the user to the uploaded_file route, which
	    #     # will basically show on the browser the uploaded file
	    #     return redirect(url_for('uploaded_file',
	    #                             filename=filename))


@app.route('/messages', methods = ['POST'])
def api_message():
	if request.headers['Content-Type'] == 'text/plain':
		return "Text Message: " + request.data

	elif request.headers['Content-Type'] == 'application/json':
		return "JSON Message: " + json.dumps(request.json)

	elif request.headers['Content-Type'] == 'application/octet-stream':
		f = open('./binary', 'wb')
		f.write(request.data)
		f.close()
		return "Binary message written!"

	else:
		return "415 Unsupported Media Type ;)"


if __name__ == "__main__":
    app.run()
