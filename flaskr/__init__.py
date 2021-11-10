from flask import Flask
from configs import config_by_name
from .models import setup_db


def create_app(config_object='development'):
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_by_name[config_object])
    # Setup DB
    setup_db(app)

    @app.get("/")
    def index():
        return "Welcome to our app"

    return app