from app import app
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DevelopmentConfig as devConfig


app.config["SQLALCHEMY_DATABASE_URI"] = devConfig.SQLALCHEMY_DATABASE_URI

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

## create db instance
db = SQLAlchemy(app)

## initialize db
db.init_app(app)

## migrate
migrate = Migrate(app, db)


class Repo(db.Model):
    __tablename__ = "repos"

    id = db.Column(db.Integer, primary_key=True)
    repo_name = db.Column(db.String(100), nullable=False)
    stars = db.Column(db.Integer, nullable=False)
    repo_url = db.Column(db.String(100), nullable=False)
    language = db.Column(db.String(20), nullable=False)

    def __init__(self, repo_name, stars, repo_url, language):
        self.repo_name = repo_name
        self.stars = stars
        self.repo_url = repo_url
        self.language = language


def create_database():
    ## Create a db engine
    db_engine = create_engine(devConfig.BASE_DB_URI)

    ## create a databse if doesn't exist
    with db_engine.connect() as conn:
        conn.execute(f"CREATE DATABASE IF NOT EXISTS {devConfig.DB_NAME}")
        # print(f"Database {devConfig.DB_NAME} is created successfully!")


def insert_data_into_db(results):
    try:
        ## creates a table
        db.create_all()
        for result in results:
            ## preparing insert statment
            insert_repo = Repo(
                repo_name=result[0],
                stars=result[1],
                repo_url=result[2],
                language=result[3],
            )

            ## inserts the records
            db.session.add(insert_repo)

        ## commit the db changes
        db.session.commit()
        # print("Data has been inserted successfully!")
    except Exception as ex:
        print(ex)


def verify_if_data_exists_in_db(language_choice):
    count = 0
    try:
        repos = Repo.query.filter_by(language=language_choice).all()
        if repos is not None:
            count = len(repos)
    except Exception as ex:
        print(ex)
    return count


def get_data_from_db(language_choice):
    try:
        ## get all the records for a given language
        repos = Repo.query.filter_by(language=language_choice).all()
        return repos
    except Exception as ex:
        print(ex)
