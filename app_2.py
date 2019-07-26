from flask import Flask


def create_flask_app(app_name):
    app = Flask(app_name)
    return app
