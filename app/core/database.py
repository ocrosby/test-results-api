from typing import Generator

from sqlalchemy.engine import Engine
from sqlmodel import Session, SQLModel, create_engine

from app.core.config import settings


def get_engine() -> Engine:
    """
    Get a new SQLAlchemy engine instance

    In your tests you can mock the get_engine function to prevent the actual engine from being created.
    :return:
    """
    return create_engine(settings.DATABASE_URL)


# Dependency to get a new session for each request
def get_session() -> Generator[Session, None, None]:
    """
    Get a new SQLAlchemy session instance

    :return:
    """
    engine = get_engine()
    with Session(engine) as session:
        yield session


def create_db_and_tables():
    """
    Create the database and tables

    :return:
    """
    engine = get_engine()
    SQLModel.metadata.create_all(engine)
