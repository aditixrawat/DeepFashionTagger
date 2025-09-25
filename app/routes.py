import os
from flask import Blueprint, render_template, request, current_app, url_for, redirect
from werkzeug.utils import secure_filename
from app.predict import predict_image

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

main = Blueprint('main', __name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    image_url = None

    if request.method == "POST":
        if 'image' not in request.files:
            return render_template("index.html", error="No file part")
        file = request.files['image']
        if file.filename == '':
            return render_template("index.html", error="No selected file")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            save_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file.save(save_path)
            prediction = predict_image(save_path)  # replace later with real model
            image_url = url_for('static', filename=f'uploads/{filename}')
        else:
            return render_template("index.html", error="File type not allowed")

    return render_template("index.html", prediction=prediction, image_url=image_url)
