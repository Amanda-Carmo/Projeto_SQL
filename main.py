from uuid import UUID
from models import Book, Genre

from typing import List, Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Banco de dados criados, por hora, em uma estrutura em python simples
db: List[Book] = [
    Book(
        id = UUID, 
        name = "Harry Potter and the Philosopher's Stone", 
        genre = Genre.fantasy, 
        author_name = "J. K. Rowling"),
        
    Book(
        id = UUID, 
        name = "The Book Thief", 
        genre = Genre.drama, 
        author_name = "Markus Zusak"),

    Book(
        id = UUID, 
        name = "Sherlock Holmnes: A Study in Scarlet", 
        genre = Genre.mystery, 
        author_name = "Arthur Conan Doyle"),
]

@app.get("/")
def read_root():
    return {"Hello": "World"}