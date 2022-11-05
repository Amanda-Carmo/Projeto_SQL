from uuid import UUID
from models import Book, BookRequest
from db import db
from typing import List
from fastapi import FastAPI, HTTPException, Body, Depends
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/api/v1/books")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}

@app.get("/")
def read_root():
    return {"Hello": "World"}

# GET
@app.get("/api/v1/books")
async def fetch_books():
    return {"Books": db}

# Post com exemplo de inserção -- 
# De modo a deixar claro que não é necessário colocar ID, já que é colocado automaticamente
@app.post("/api/v1/books")
async def register_book(book: Book = Body(
        example={
            "name": "The Chronicles of Narnia",
            "genre": "fantasy",
            "author_name": "C. S. Lewis",
            "price": 35.4},
    ),):
    db.append(book)                                                         # RETURN : mostra que o registro funcionou
    return {"task": "register successful", "name":book.name, "id": book.id} # e mostra nome e id do livro

# Deletando um livro
@app.delete("/api/v1/books/{books_id}")
async def delete_book(book_id: UUID):
    for book in db:
        if book.id == book_id:
            db.remove(book)
            return {"task": "delete successful", "book": book.name} # Mostra avisa que o delete teve sucesso
    raise HTTPException(status_code=404, detail=f"book with id: {book_id} does not exists")

# Atualização de dados de um livro
@app.put("/api/v1/books/{book_id}")
async def update_book(book_id: UUID, book_update: BookRequest):
    for book in db:
        if book.id == book_id: # checa se o id está correto
            # Conferindo qual dado foi alterado
            if book_update.name:
                book.name = book_update.name
            if book_update.genre:
                book.genre = book_update.genre
            if book_update.author_name:
                book.author_name = book_update.author_name
            if book_update.price:
                book.price = book_update.price
            if book_update.amount:
                book.amount = book_update.amount
            return book
    raise HTTPException(status_code=404, detail=f"book with id: {book_id} does not exists")