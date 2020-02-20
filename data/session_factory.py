import urllib
import pyodbc
from contextlib import contextmanager

import sqlalchemy
import sqlalchemy.orm
import db.db_folder as db_folder
from models.model_base import ModelBase
# noinspection PyUnresolvedReferences
from models import storage, item


__factory = None


def global_init():
    global __factory

    # full_file = db_folder.get_db_path('food_helper.sqlite.db')
    # connection_string = 'sqlite:///' + full_file

    params = urllib.parse.quote_plus(r'Driver={ODBC Driver 13 for SQL Server};Server=tcp:food-helper-server.database.windows.net,1433;Database=food_helper_db;Uid=<user>;Pwd=<password>;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    connection_string = 'mssql+pyodbc:///?odbc_connect={}'.format(params)

    engine = sqlalchemy.create_engine(connection_string, echo=True)
    ModelBase.metadata.create_all(engine)

    __factory = sqlalchemy.orm.sessionmaker(bind=engine)


@contextmanager
def get_session():

    try:
        session = create_session()
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def create_session():
    global __factory

    if __factory is None:
        global_init()

    return __factory()
