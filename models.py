import os 
from sqlalchemy import create_engine, TypeDecorator
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.schema import Column
from sqlalchemy import ForeignKey
from sqlalchemy.types import String, Integer, Float, Date, Numeric, Enum, Text
import models as schemas
from sqlalchemy import desc
from sqlalchemy.dialects.postgresql import UUID
import uuid
from schemas import Genre

from database import Base

import datetime

def _get_date():
    return datetime.datetime.now()
 
class Book(Base):
    __tablename__ = "Book"
    # id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    book_name = Column(String(80), primary_key=True, nullable=False)
    genre = Column(String(36), nullable=False)
    author_name = Column(String(50))
    price = Column(Numeric)
    amount = Column(Integer, default=0)

    order = relationship("Order", back_populates="book")
    purchase = relationship("Purchase", back_populates="book")

# Venda de livros (saída)
class Order(Base):
    __tablename__ = "Order"
    user_id = Column(Integer, default=1, nullable=False) #usuário que pediu

    order_id = Column(Integer, primary_key=True, default="a")
    book_name = Column(String(length=80), ForeignKey("Book.book_name"), nullable=False)
    amount = Column(Integer, nullable=False)
    order_date = Column(Date, onupdate=_get_date)

    book = relationship("Book", back_populates="order")

# Compra de livros (recolocar no estoque)
class Purchase(Base):
    __tablename__ = "Purchase"
    user_id = Column(Integer, default=1, nullable=False) #usuário que vendeu

    purchase_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    book_name = Column(String(length=80), ForeignKey("Book.book_name"), nullable=False)
    amount = Column(Integer, nullable=False)
    purchase_date = Column(Date, onupdate=_get_date)

    book = relationship("Book", back_populates="purchase")