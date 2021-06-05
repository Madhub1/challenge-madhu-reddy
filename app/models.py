from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    insert,
)
import pymysql


## MySQLdb module
pymysql.install_as_MySQLdb()


class Repo:
    def __init__(self):
        self.user_id = "root"
        self.password = "superdb.1"
        # self.host = "localhost"  ## used when running the app locally
        self.host = "db"  ## when running the app in docker container
        self.port = 3306
        self.DB_NAME = "repos_db"
        self.table_name = "repos"
        self.db_uri = f"mysql+pymysql://{self.user_id}:{self.password}@{self.host}:{self.port}/{self.DB_NAME}"
        ## create an engine with the
        self.engine = create_engine(self.db_uri)

    def create_database(self):
        print("create_database is invoked")
        try:
            base_db_uri = f"mysql+pymysql://{self.user_id}:{self.password}@{self.host}:{self.port}"

            ## Create a db engine
            db_engine = create_engine(base_db_uri)

            ## create a databse if doesn't exist
            with db_engine.connect() as conn:
                conn.execute(f"CREATE DATABASE IF NOT EXISTS {self.DB_NAME}")
                print(f"database {self.DB_NAME} is created successfully!")

        except Exception as ex:
            print(ex)

    def insert_data_into_db(self, results: list):
        print("insert_data_into_db is invoked")
        try:
            with self.engine.connect() as conn:
                conn.execute(f"USE {self.DB_NAME}")
                print(f"using {self.DB_NAME} database")

                ## Create a metadata instance
                metadata = MetaData(self.engine)

                ## Declare a table
                table = Table(
                    self.table_name,
                    metadata,
                    Column("id", Integer, primary_key=True),
                    Column("repo_name", String(100)),
                    Column("stars", Integer),
                    Column("repo_url", String(100)),
                    Column("language", String(20)),
                )

                ## Create all tables
                metadata.create_all(self.engine)

                ## Prepare an insert statement
                insert_stmt = insert(table).values(results)

                ## execute insert statement
                conn.execute(insert_stmt)
        except Exception as ex:
            print(ex)

    def verify_if_data_exists_in_db(self, language_choice: str):
        print("verify_if_data_exists_in_db is invoked")
        count = 0
        try:
            with self.engine.connect() as conn:
                ## use the specific database
                self.engine.execute(f"USE {self.DB_NAME}")
                print(f"using {self.DB_NAME} database")

                ## Prepare select statement
                select_stmt = f"select count(*) from {self.table_name} where language = '{language_choice}';"

                ## execute select statement
                result = conn.execute(select_stmt)

                ## get the count of rows in database for the given language
                for _row in result:
                    count = _row[0]
        except Exception as ex:
            print(ex)
        return count

    def get_data_from_db(self, language_choice: str):
        print("get_data_from_db is invoked")
        records = []
        try:
            with self.engine.connect() as conn:
                ## use the specific database
                self.engine.execute(f"USE {self.DB_NAME}")
                print(f"using {self.DB_NAME} database")

                ## Prepare select statement
                select_stmt = f"select * from {self.table_name} where language = '{language_choice}' order by stars desc;"

                ## execute select statement
                records = conn.execute(select_stmt)
        except Exception as ex:
            print(ex)

        ## return the data for the given language from the database
        return records
