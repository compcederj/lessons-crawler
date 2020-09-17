import os

from dotenv import load_dotenv
from sqlalchemy import (
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    Time,
    Unicode,
    Text,
    JSON,
    create_engine,
    func,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

from lessons_crawler.helpers.meta_singleton import MetaSingleton

load_dotenv()

Session = sessionmaker()
Base = declarative_base()

DbEnum = Enum


class Database(metaclass=MetaSingleton):
    engine = create_engine(os.getenv("DB_URI"))
    session = Session(bind=engine)


db = Database()
