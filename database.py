from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

session = None


def create_db_engine(database_url):
    engine = create_engine(database_url)
    return engine


def get_session(database_url):
    global session
    engine = create_db_engine(database_url)
    session_factory = sessionmaker(bind=engine)
    session = scoped_session(session_factory)()
    return session
