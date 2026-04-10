from flask import Flask
from flask_cors import CORS
from .routes.auth import auth_bp
from .routes.video import video_bp
from .routes.image import image_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(video_bp)
    app.register_blueprint(image_bp)

    return app
