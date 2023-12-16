import os
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    """
    Check if the file extension is allowed.
    """
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def save_uploaded_file(file, upload_folder):
    """
    Save the uploaded file to the specified upload folder.
    """
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(upload_folder, filename))
        return True, filename
    return False, None
