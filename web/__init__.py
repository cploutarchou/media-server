from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import os
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = '/home/media'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



# Logging Configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
handler = RotatingFileHandler('web.log', maxBytes=10000, backupCount=3)
logger.addHandler(handler)

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        # Change 'file' to 'myFile' to match the MultipartEncoder field
        if 'myFile' not in request.files:
            raise ValueError("No myFile part")

        file = request.files['myFile']
        if file.filename == '':
            raise ValueError("No selected file")


        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return jsonify(success=True, filename=filename), 200


    except Exception as e:
        logger.error(f"Error during upload: {str(e)}")
        return jsonify(error=str(e)), 500

@app.route('/<path:filename>', methods=['GET'])
def get_image(filename):
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    except FileNotFoundError:
        logger.error(f"File not found: {filename}")
        return jsonify(error="File not found"), 404


if __name__ == '__main__':
    app.run(debug=True)
