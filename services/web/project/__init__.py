from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from project.config import create_config

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_class=None):
    config = create_config(config_class=config_class)

    app = Flask(__name__)

    app.config.from_object(config)

    bootstrap.init_app(app)
    db.init_app(app)

    from project.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from project.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
