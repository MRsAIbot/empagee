from flask import Flask
from flask import render_template, request, redirect, url_for, send_from_directory, json
from werkzeug.utils import secure_filename

import base64
import os

from googleapiclient import discovery
import httplib2
import json
from oauth2client.client import GoogleCredentials

app = Flask(__name__)

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'uploads/')
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

DISCOVERY_URL = 'https://{api}.googleapis.com/$discovery/rest?version={apiVersion}'


# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


def get_vision_service():
    credentials = GoogleCredentials.get_application_default()
    return discovery.build('vision', 'v1', credentials=credentials,
                           discoveryServiceUrl=DISCOVERY_URL)


def detect_face(face_file, max_results):
    image_content = face_file
    batch_request = [{
        'image': {
            'content': base64.b64encode(image_content).decode('UTF-8')
        },
        'features': [{
            'type': 'FACE_DETECTION',
            'maxResults': max_results,
        }]
    }]

    service = get_vision_service()
    request = service.images().annotate(body={
        'requests': batch_request,
    })
    response = request.execute()

    return response['responses'][0]['faceAnnotations']


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


@app.route("/affect/<filname>")
def get_affect(filename):
    return 0


# # Route that will process the file upload
# @app.route('/upload', methods=['POST'])
# def upload():
#     if request.headers['Content-Type'] == 'text/html':
#         imgstr = request.data
#         output = open('uploads/output.png', 'wb')
#
#         output.write(imgstr.decode('base64'))
#
#         output.close()
#         return "JSON Message: " + request.data


# Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
    imgstr = request.data
    decodedImg = imgstr.decode('base64')

    # Get the name of the uploaded file
    # file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    # if file and allowed_file(file.filename):
    #     # Make the filename safe, remove unsupported chars
    #     filename = secure_filename(file.filename)
    #     # Move the file form the temporal folder to
    #     # the upload folder we setup
    #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    # Call Google Vision API
    # with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'rb') as face_file:
    annotation = detect_face(decodedImg, 1)
    print annotation
    # return annotation
    # Redirect the user to the uploaded_file route, which
    # will basically show on the browser the uploaded file
    return "Aap"
    # return redirect(url_for('uploaded_file',
    #                         filename=filename))


# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads
# an image, that image is going to be show after the upload
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


if __name__ == "__main__":
    app.debug = True
    app.run()
