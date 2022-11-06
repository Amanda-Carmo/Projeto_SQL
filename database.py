import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy_utils import database_exists
from sqlalchemy_utils.functions.database import create_database

# Create a database URL for SQLAlchemy ¶
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
SQLALCHEMY_DATABASE_URL = os.getenv("DB_CONN")

# if not SQLALCHEMY_DATABASE_URL:
#     raise Exception("Could not load environment variable 'SQLALCHEMY_DATABASE_URL'.")

engine = create_engine(SQLALCHEMY_DATABASE_URL)

if not database_exists(engine.url):
    print(f"Created database '{os.getenv('DB_DATABASE_NAME')}'")
    create_database(engine.url)

# print(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()

# dependency
def get_db():
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()