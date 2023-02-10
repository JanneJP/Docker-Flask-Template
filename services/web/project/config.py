import os

from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    STATIC_FOLDER = f"{os.getenv('APP_FOLDER')}/project/static"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class PytestConfig(TestingConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///pytest.db'


class ProductionConfig(Config):
    pass


def create_config(config_class=None):
    load_dotenv()

    configs = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'pytest': PytestConfig,
        'production': ProductionConfig
    }

    env_config = os.getenv('APP_ENV')

    config_class_name = config_class if config_class else env_config if env_config else 'development'

    config = configs.get(config_class_name)

    return config
