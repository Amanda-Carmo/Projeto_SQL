from uuid import UUID
from models import Book
from typing import List
from fastapi import FastAPI, HTTPException, Body, Depends, Header
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm.session import Session
from database import get_db
from crud import *
from database import Base, engine

from fastapi.params import Path

from schemas import BookUpdate
import asyncio

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

# ------------------------------------------------------------- CRUD DOS LIVROS -------------------------------------------------------------

# GET toda a tabela, com todos os livros
@app.get("/api/v1/books")
async def fetch_books(db:Session = Depends(get_db)):
    books = get_books(db)
    return books

# GET pega informação de um livro específico
@app.get("/api/v1/books/{book_name}")
async def fetch_book(book_name: str, db:Session = Depends(get_db)):
    name = get_book_byname(db, book_name)
    if name is not None:
        return name
    raise HTTPException(404, f"Book with name {book_name} does not exists")

# Registrar mais um livro na loja
# Post com exemplo de inserção -- 
# De modo a deixar claro que não é necessário colocar ID, já que é colocado automaticamente
@app.post("/api/v1/books")
async def register_book(book_created: schemas.BookCreate = Body(
        example={
            "book_name": "The Chronicles of Narnia",
            "genre": "fantasy",
            "author_name": "C. S. Lewis",
            "price": 35.4},
    ), db: Session = Depends(get_db),):

    #checa se livro já existe 
    book_exists = get_book_byname(db, book_created.book_name) is not None
    if book_exists:
        raise HTTPException(400, "Book already in inventory")

    book = create_book(db, book_created)                                    # RETURN : mostra que o registro funcionou
    return {"task": "register successful", "name":book.book_name} # e mostra nome e id do livro

 # Delete Book
@app.delete("/api/v1/books/{book_name}")
async def remove_book(book_name: str, db: Session = Depends(get_db)):
    try:
        delete_book(db, book_name)
        return {"task": "delete successful"}
    except:
        raise HTTPException(status_code=404, detail=f"book with name: {book_name} does not exists")

# Atualização do preço de um livro (pode ter uma promoção, por exemplo...)
@app.put("/api/v1/books/{book_name}")
async def update_books(book_name: str, book_updated: schemas.BookUpdate = Body(
        example={
            "price": 35.4,},
    ), db: Session = Depends(get_db)):

    
    book = update_book(db, book_name, book_updated)
    if book is not None:
        return book_updated

    raise HTTPException(status_code=404, detail=f"book with name: {book_name} does not exists")


# -------------------------------------------------------------------- CRUD PARA ORDERS E PURCHASES --------------------------------------------

# Tabela com informações de todas as saídas de livros para controle
# GET
@app.get("/api/v1/orders")
async def get_orders(db:Session = Depends(get_db)):
    orders = get_order(db)
    return orders

# Deletando uma order (vai que ocorra algum erro buocrático...)
@app.delete("/api/v1/orders/{order_id}")
async def remove_order(order_id: int, db: Session = Depends(get_db)):

    delete_order(db, order_id)
    return {"task": "delete successful"} # Mostra avisa que o delete teve sucesso
   
# Cria uma nova venda
# Post
@app.post("/api/v1/orders")
async def register_order(order_created: schemas.OrderCreate = Body(
        example={
            "user_id": 3,
            "book_name": "The Book Thief",
            "amount": 15,
            "order_date": "2022-11-23"},
    ), db: Session = Depends(get_db)):
     
    db_book = models.Book

    # Para checar se livro existe
    book_exists = get_book_byname(db, order_created.book_name) is not None
    if book_exists:
        order = create_order(db, order_created) 
        update_amount_order(db, order_created.book_name, db_book, order_created.amount) 
        return order  
    
    else:
        raise HTTPException(status_code=404, detail=f"book with name {order_created.book_name} does not exists")
                
    
# Tabela com informações de todas as entradas de livros para controle
# GET
@app.get("/api/v1/purchases")
async def get_purchases(db:Session = Depends(get_db)):
    purchases = get_purchase(db)
    return purchases

# Cria uma nova compra
# Post
@app.post("/api/v1/purchases")
async def register_purchase(purchase_created: schemas.PurchaseCreate = Body(
        example={
            "user_id": 3,
            "book_name": "The Book Thief",
            "amount": 15,
            "purchase_date": "2022-11-23"},
        ), db: Session = Depends(get_db),):

        db_book = models.Book
        
        # Para checar se livro existe
        book_exists = get_book_byname(db, purchase_created.book_name) is not None
        if book_exists:    
            purchase = create_purchase(db, purchase_created) 
            update_amount_purchase(db, purchase_created.book_name, db_book, purchase_created.amount)

            return purchase  
        
        raise HTTPException(status_code=404, detail=f"book with name {purchase_created.book_name} does not exists")
        

# Deletando Purchase (vai que ocorra algum erro burocrático)
@app.delete("/api/v1/purchases/{purchase_id}")
async def remove_purchase(purchase_id: int, db: Session = Depends(get_db)):
    try:
        delete_purchase(db, purchase_id)
        return {"task": "delete successful"} # Mostra avisa que o delete teve sucesso
    except:
        raise HTTPException(status_code=404, detail=f"purchase with id: {purchase_id} does not exists")


Base.metadata.create_all(bind=engine)