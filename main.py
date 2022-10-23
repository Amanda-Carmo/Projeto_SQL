from uuid import UUID, uuid4
from models import Book, Genre

from typing import List, Union

from fastapi import FastAPI

app = FastAPI()

# Banco de dados criados, por hora, em uma estrutura em python simples
db: List[Book] = [
    Book(
        id = UUID("e57957c5-72f8-4a83-b609-52ed7c0505f4"), 
        name = "Harry Potter and the Philosopher's Stone", 
        genre = Genre.fantasy, 
        author_name = "J. K. Rowling"),
        
    Book(
        id = UUID("8dc377f9-912f-469e-a4d6-baf0f734d6ce"), 
        name = "The Book Thief", 
        genre = Genre.drama, 
        author_name = "Markus Zusak"),

    Book(
        id = UUID("7d41c58f-939f-4c2e-be84-724fcfa22b79"), 
        name = "Sherlock Holmnes: A Study in Scarlet", 
        genre = Genre.mystery, 
        author_name = "Arthur Conan Doyle"),
]

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