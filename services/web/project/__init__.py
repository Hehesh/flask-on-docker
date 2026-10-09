import os

from flask import request, send_from_directory, abort, Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, email):
        self.email = email


@app.route("/")
def hello_world():
    return jsonify(hello="world")

@app.route("/media/<path:filename>")
def mediafiles(filename):
    return send_from_directory(app.config["MEDIA_FOLDER"], filename)


@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files.get("file")

        if file is None or not file.filename:
            abort(400, description="No file selected")

        filename = secure_filename(file.filename)

        if not filename:
            abort(400, description="Invalid filename")

        os.makedirs(app.config["MEDIA_FOLDER"], exist_ok=True)

        file.save(os.path.join(app.config["MEDIA_FOLDER"], filename))

        return f"Uploaded successfully: {filename}", 201

    return """
    <!doctype html>
    <html>
        <head>
            <title>Upload File</title>
        </head>
        <body>
            <h2>Upload a File</h2>
            <form method="POST" enctype="multipart/form-data">
                <input type="file" name="file">
                <input type="submit" value="Upload">
            </form>
        </body>
    </html>
    """
