# from typing import Generator
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
# from config import settings

# engine = create_engine(settings.DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# def get_db() -> Generator:
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = None

def init_db(app: Flask):
    global db 
    db = SQLAlchemy(app)