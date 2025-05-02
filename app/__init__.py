# app/__init__.py
from flask import Flask, render_template
from app.api import api

def create_app():
    app = Flask(__name__)

    # Register the API blueprint
    app.register_blueprint(api, url_prefix='/api')

    # Route to serve the webpage
    @app.route('/')
    def home():
        return render_template('index.html')

    return app
