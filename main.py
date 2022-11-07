from uuid import UUID
from models import Book
from typing import List
from fastapi import FastAPI, HTTPException, Body, Depends
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm.session import Session
from database import get_db
from crud import *
from database import Base, engine

from schemas import BookUpdate

app = FastAPI()

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# @app.get("/api/v1/books")
# async def read_items(token: str = Depends(oauth2_scheme)):
#     return {"token": token}

@app.get("/")
def read_root():
    return {"Hello": "World"}

# GET
@app.get("/api/v1/books")
async def fetch_books(db:Session = Depends(get_db)):
    books = get_books(db)
    return books

# GET
@app.get("/api/v1/books/{book_name}")
async def fetch_books(book_name: str, db:Session = Depends(get_db)):
    book_name = get_book_byname(db, book_name)
    return book_name

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

 
# Deletando um livro
@app.delete("/api/v1/books/{book_name}")
async def delete_book(book_name: str, db: Session = Depends(get_db)):
    try:
        delete_book(db, book_name)
        return {"task": "delete successful"} # Mostra avisa que o delete teve sucesso
    
    except:
        raise HTTPException(status_code=404, detail=f"book with name: {book_name} does not exists")



# Atualização do preço de um livro
@app.put("/api/v1/books/{book_name}")
async def update_book(book_name: str, book_updated: schemas.BookUpdate = Body(
        example={
            "price": 35.4,
            "amount": 2},
    ), db: Session = Depends(get_db)):

    # try:
    book_update = update_book(db, book_name, book_updated)
    print(book_update)
    return {"task": "update successful", "name":book_name} 
    # except:
    #     raise HTTPException(status_code=404, detail=f"book with id: {book_name} does not exists")


# -------------------------------------------------------------------------------------------------------------

# GET
@app.get("/api/v1/orders")
async def get_orders(db:Session = Depends(get_db)):
    orders = get_order(db)
    return orders

# GET
@app.get("/api/v1/purchases")
async def get_purchases(db:Session = Depends(get_db)):
    purchases = get_purchase(db)
    return purchases

# Post
@app.post("/api/v1/orders")
async def register_order(order_created: schemas.OrderCreate = Body(
        example={
            "user_id": 3,
            "book_name": "The Book Thief",
            "amount": 15,
            "order_date": 2022-11-23},
    ), db: Session = Depends(get_db)):

    try:
        order = create_order(db, order_created)                        # RETURN : mostra que o registro funcionou
        return order

    except:
        raise HTTPException(status_code=404, detail=f"book with name: {order_created.book_name} does not exists")

# Post
@app.post("/api/v1/purchases")
async def register_purchase(purchase_created: schemas.PurchaseCreate = Body(
        example={
            "user_id": 3,
            "book_name": "The Book Thief",
            "amount": 15,
            "purchase_date": 2022-11-23},
    ), db: Session = Depends(get_db),):

    try:
        purchase = create_purchase(db, purchase_created)   
        return purchase  
    except:
        raise HTTPException(status_code=404, detail=f"book with name: {purchase_created.book_name} does not exists")

    # RETURN : mostra que o registro funcionou

Base.metadata.create_all(bind=engine)