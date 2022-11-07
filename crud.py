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
def delete_book(db: Session, book_name: str) -> str:
    book = db.query(models.Book).filter(models.Book.book_name == book_name).first()
    # if book is not None:
    db.delete(book)
    db.commit()    
    
# Atualizar preço
def update_book(db: Session, book_name: str, book_update: schemas.BookUpdate):
    db.query(models.Book).filter(models.Book.book_name == book_name).update(book_update.dict(), synchronize_session="fetch")
    db.commit()
    return get_book_byname(db, book_name)

# Read de multiplas orders
def get_order(db: Session) -> list[schemas.Order]:
    return db.query(models.Order).all()

# Read de multiplas purchases
def get_purchase(db: Session) -> list[schemas.Purchase]:
    return db.query(models.Purchase).all()

# Criar order
def create_order(db: Session, db_order: schemas.OrderCreate) -> schemas.OrderCreate:
    db_order = models.Order(**db_order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

# Criar purchase
def create_purchase(db: Session, db_purchase: schemas.PurchaseCreate) -> schemas.PurchaseCreate:
    db_purchase = models.Purchase(**db_purchase.dict())
    db.add(db_purchase)
    db.commit()
    db.refresh(db_purchase)
    return db_purchase

# Deletar Order
def delete_order(db: Session, order_id: int) -> int:
    order = db.query(models.Order).filter(models.Order.order_id == order_id).first()
    # if book is not None:
    db.delete(order)
    db.commit()    
    
# Deletar Order
def delete_purchase(db: Session, purchase_id: int) -> int:
    purchase = db.query(models.Purchase).filter(models.Purchase.purchase_id == purchase_id).first()
    # if book is not None:
    db.delete(purchase)
    db.commit() 