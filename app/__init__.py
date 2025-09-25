import os
from flask import Flask

def create_app():
    app = Flask(__name__, 
                static_folder='static',        # serves /static/ from app/static
                template_folder='templates')   # loads app/templates

    # absolute path for uploads (inside app/static/uploads)
    upload_folder = os.path.join(app.root_path, 'static', 'uploads')
    os.makedirs(upload_folder, exist_ok=True)
    
    app.config['UPLOAD_FOLDER'] = upload_folder
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit

    from .routes import main
    app.register_blueprint(main)

    return app
