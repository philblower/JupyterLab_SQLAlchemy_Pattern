import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
print(f"basedir = {basedir}")

class Config:
    # for mysql database
    DB_USERNAME = os.environ.get('DB_USERNAME')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')


class DevelopmentConfig(Config):
    DB1 = 'chinook.sqlite'
    DB2 = 'pab.sqlite'

    # sqlite database URLs
    DB1_URL = "sqlite:///" + os.path.join(basedir, DB1)
    DB2_URL = "sqlite:///" + os.path.join(basedir, DB2)

    # example mysql database URLs
    # DB1_URL = f"mysql+mysqlconnector://{Config.DB_USERNAME}:{Config.DB_PASSWORD}@localhost/{DB1}"
    # DB2_URL = f"mysql+mysqlconnector://{Config.DB_USERNAME}:{Config.DB_PASSWORD}@localhost/{DB2}"


class ProductionConfig(Config):
    # Use the same databases as DevelopmentConfig in this simple example.
    # For production these would be set to the production database.
    DB1 = 'chinook.sqlite'
    DB2 = 'pab.sqlite'

    # sqlite database URLs
    DB1_URL = "sqlite:///" + os.path.join(basedir, DB1)
    DB2_URL = "sqlite:///" + os.path.join(basedir, DB2)

    # example mysql database URLs
    # DB1_URL = f"mysql+mysqlconnector://{Config.DB_USERNAME}:{Config.DB_PASSWORD}@localhost/{DB1}"
    # DB2_URL = f"mysql+mysqlconnector://{Config.DB_USERNAME}:{Config.DB_PASSWORD}@localhost/{DB2}"

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

""" Configure sqlalchemy session and engines
"""
Session = sessionmaker()
session = None
engine1 = None
engine2 = None
binds = None

Base1 = declarative_base() # db1 classes
Base2 = declarative_base() # db2 classes

def set_engines(config):
    global engine1, engine2, binds
    engine1 = create_engine(config.DB1_URL)
    engine2 = create_engine(config.DB2_URL)
    binds={Base1:engine1, Base2:engine2}

def set_session():
    """ Initialize session after engines and binds are defined.

    Parameters
    ----------
    binds : dict
        dict of engines

    Returns
    -------
    None : sets value of the session global
    """
    global session, binds
    session = Session(binds=binds)

def get_engine(class_):
    """ Return the engine for this class/table

    Parameters
    ----------
    class_ : model.py class

    Returns
    -------
    engine : Sqlalchemy connection engine to sql database
    """
    return session.get_bind(mapper=class_)
