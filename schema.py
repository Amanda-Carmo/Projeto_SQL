import os 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.schema import Column
from sqlalchemy import ForeignKey
from sqlalchemy.types import String, Integer, Float, Date, Numeric
import models as schemas
from sqlalchemy import desc

from database import Base

import datetime

def _get_date():
    return datetime.datetime.now()

class Genre(Base):
    __tablename__ = "Genres"
    name = Column(String, primary_key=True)

class Book(Base):
    __tablename__ = "Books"
    id = Column(String, nullable=False, primary_key=True)
    name = Column(String)
    genre = Column(String, ForeignKey("Genre.name"), nullable=False)
    author_name = Column(String)
    price = Column(Numeric)
    amount = Column(Integer)


class Order(Base):
    __tablename__ = "Order"
    id = Column(String, primary_key=True)
    book_id = Column(String, ForeignKey("Book.id"), nullable=False)
    amount = Column(Integer)
    order_date = Column(Date, onupdate=_get_date)

    book = relationship("Book")

class Purchase(Base):
    __tablename__ = "Purchase"
    id = Column(String, primary_key=True)
    book_id = Column(String, ForeignKey("Book.id"), nullable=False)
    amount = Column(Integer)
    purchase_date = Column(Date, onupdate=_get_date)

    book = relationship("Book")