import uuid
from typing import Optional

from sqlalchemy.orm import Session

import models, schemas

# Read de multiplos livros
def get_books(db: Session) -> list[schemas.Book]:
    return db.query(models.Book).all()

# Read book by its name
def get_book_byname(db: Session, name: str) -> Optional[schemas.Book]:
    return db.query(models.Book).filter(models.Book.book_name == name).first()
    
# Criar um livro
def create_book(db: Session, db_book: schemas.BookCreate) -> schemas.BookCreate:
    db_book = models.Book(**db_book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# Deletar um livro
def delete_book(db: Session, name: str):
    book = db.query(models.Book).filter(models.Book.book_name == name).first()
    db.delete(book)
    db.commit()

def update_book(db: Session, book_name: str, book_update: schemas.BookUpdate) -> Optional[schemas.Book]:
    db.query(models.Book).filter(models.Book.book_name == book_name).update(book_update.dict(), synchronize_session="fetch")
    db.commit()
    return get_books(db, book_name, book_update.price)


 
# def get_purchases(db: Session, skip: int = 0, limit: int = 50):
#     return db.query(models.Purchase).offset(skip).limit(limit).all()

# def get_orders(db: Session, skip: int = 0, limit: int = 50):
#     return db.query(models.Order).offset(skip).limit(limit).all()

# Read de multiplas orders
def get_order(db: Session) -> list[schemas.Order]:
    return db.query(models.Order).all()

# Read de multiplas purchases
def get_purchase(db: Session) -> list[schemas.Purchase]:
    return db.query(models.Purchase).all()

# # Read book by its name
# def get_book_byname(db: Session, name: str) -> Optional[schemas.Book]:
#     return db.query(models.Book).filter(models.Book.book_name == name).first()

# Criar order
def create_order(db: Session, db_order: schemas.OrderCreate) -> schemas.OrderCreate:
    db_order = models.Order(**db_order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

# Criar purchase
def create_purchase(db: Session, db_purchase: schemas.PurchaseCreate) -> schemas.PurchaseCreate:
    db_purchase = models.Order(**db_purchase.dict())
    db.add(db_purchase)
    db.commit()
    db.refresh(db_purchase)
    return db_purchase

# def buy_book():

# def sell_book():
