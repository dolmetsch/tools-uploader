import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'uploads')
ALLOWED_EXTENSIONS = { 'mp3', }

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/record-word-mp3', methods=['POST'])
def upload_file():
    print(UPLOAD_FOLDER)
    if 'word' not in request.form:
        return '{ "error": "no word" }'
    if 'mp3' not in request.files:
        return '{ "error": "no audio file" }'
    file = request.files['mp3']
    language = request.form['language']
    if file.filename == '':
        return '{ "error": "no audio file" }'
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # filename = request.form['word'] + '.mp3'
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], language, filename))
        return '{ "success": true }'
