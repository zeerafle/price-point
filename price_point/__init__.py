import os

from flask import Flask
from flask_cors import CORS

# import blueprint
from .routes.price_scraping.controllers import price_scraping


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    CORS(app)
    # register blueprint
    app.register_blueprint(price_scraping)

    @app.route('/')
    def index():
        return 'PricePoint Backend API Gateway'

    return app
