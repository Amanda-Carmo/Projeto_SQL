import os
from dotenv import dotenv_values

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy_utils import database_exists
from sqlalchemy_utils.functions.database import create_database

env = dict(dotenv_values(".env")) 

# Create a database URL for SQLAlchemy ¶
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# SQLALCHEMY_DATABASE_URL = os.getenv("DB_CONN")
DB_CONNECTION_STRING = env.get("DB_CONNECTION_STRING")

# if not SQLALCHEMY_DATABASE_URL:
#     raise Exception("Could not load environment variable 'SQLALCHEMY_DATABASE_URL'.")

engine = create_engine(DB_CONNECTION_STRING)
 
if not database_exists(engine.url):
    print(f"Created database '{env.get('DB_DATABASE_NAME')}'")
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