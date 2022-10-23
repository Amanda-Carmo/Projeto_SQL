from uuid import UUID
from models import Book, BookRequest
from db import db

from typing import List

from fastapi import FastAPI, HTTPException, Body

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/v1/books")
async def fetch_books():
    return {"Books": db}

@app.post("/api/v1/books")
async def register_book(book: Book = Body(
        example={
            "name": "The Chronicles of Narnia",
            "genre": "fantasy",
            "author_name": "C. S. Lewis",
            "price": 35.4},
    ),):
    db.append(book)
    return {"task": "register successful", "name":book.name}

@app.delete("/api/v1/books/{books_id}")
async def delete_book(book_id: UUID):
    for book in db:
        if book.id == book_id:
            db.remove(book)
            return {"task": "delete successful", "book": book.name}
    raise HTTPException(status_code=404, detail=f"book with id: {book_id} does not exists")

@app.put("/api/v1/books/{book_id}")
async def update_book(book_id: UUID, book_update: BookRequest):
    for book in db:
        if book.id == book_id:
            if book_update.name:
                book.name = book_update.name
            if book_update.genre:
                book.genre = book_update.genre
            if book_update.author_name:
                book.author_name = book_update.author_name
            return book
    raise HTTPException(status_code=404, detail=f"book with id: {book_id} does not exists")