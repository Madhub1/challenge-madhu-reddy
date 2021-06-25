import os

# basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "super key"
    DB_USER_ID = "root"
    DB_PWD = "superdb.1"
    # DB_HOST = "localhost"
    DB_HOST = "db"  ## when deploying/running the container
    DB_PORT = 3306
    DB_NAME = "repos_db"
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER_ID}:{DB_PWD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    BASE_DB_URI = f"mysql+pymysql://{DB_USER_ID}:{DB_PWD}@{DB_HOST}:{DB_PORT}"


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
