from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("DATABASE_URL")
engine = create_engine(url=URL, future=True)

local_session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def create_all_tables():
    return Base.metadata.create_all(bind=engine)

def get_db():
    db=local_session()
    try:
        yield db
    finally:
        db.close()
