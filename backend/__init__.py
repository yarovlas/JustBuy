from flask import Flask
from config import Config
from models import db
from flask_wtf.csrf import CSRFProtect
import os

csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.secret_key = os.urandom(24)  # Ensure a secret key is set for session management

    db.init_app(app)
    
    csrf.init_app(app)  # Initialize CSRF protection

    with app.app_context():
        db.create_all()

    return app
