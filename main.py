from uuid import UUID
from models import Book, Genre
from db import db

from typing import List

from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/v1/books")
async def fetch_books():
    return db

@app.post("/api/v1/books")
async def register_book(book: Book):
    db.append(book)
    return {"id": book.id}

@app.delete("/api/v1/books/{books_id}")
async def delete_book(book_id: UUID):
    for book in db:
        if book.id == book_id:
            db.remove(book)
            return
    raise HTTPException(status_code=404, detail=f"book with id: {book_id} does not exists")