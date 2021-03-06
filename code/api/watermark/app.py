import os

from flask import Flask

from .config import config
from .models import db

def create_app(config_name=None):
    app = Flask(__name__)

    config_name = config_name or os.getenv('WM_CONFIG_ENV') or 'default'
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    from .v1 import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/v1')

    @app.route('/')
    def index():
        return "Welcome to Watermark"

    return app
