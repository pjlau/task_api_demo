# app/__init__.py
from flask import Flask
from app.api import api

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api, url_prefix='/api')
    return app
