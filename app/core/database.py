import os

from dotenv import load_dotenv
from sqlmodel import Session, create_engine

# Load environment variables from a .env file
load_dotenv()

# Get individual components of the database URL from environment variables
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("POSTGRES_HOST")
port = os.getenv("POSTGRES_PORT")
db_name = os.getenv("POSTGRES_DB")

# Construct the database URL iteratively
DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"


def get_engine():
    """
    Get a new SQLAlchemy engine instance

    In your tests you can mock the get_engine function to prevent the actual engine from being created.
    :return:
    """
    return create_engine(DATABASE_URL)


# Dependency to get a new session for each request
def get_session():
    engine = get_engine()
    with Session(engine) as session:
        yield session
