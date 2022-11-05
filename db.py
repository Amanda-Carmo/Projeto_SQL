from models import Book, Genre
from uuid import UUID
from typing import List

# Banco de dados criados, por hora, em uma estrutura em python simples
db: List[Book] = [
    Book(
        id = UUID("e57957c5-72f8-4a83-b609-52ed7c0505f4"), 
        name = "Harry Potter and the Philosopher's Stone", 
        genre = Genre.fantasy, 
        author_name = "J. K. Rowling",
        price = 36.91, 
        amount = 10),
        
    Book(
        id = UUID("8dc377f9-912f-469e-a4d6-baf0f734d6ce"), 
        name = "The Book Thief", 
        genre = Genre.drama, 
        author_name = "Markus Zusak",
        price = 12.80, 
        amount = 25),

    Book(
        id = UUID("7d41c58f-939f-4c2e-be84-724fcfa22b79"), 
        name = "Sherlock Holmnes: A Study in Scarlet", 
        genre = Genre.mystery, 
        author_name = "Arthur Conan Doyle",
        price = 12.80, 
        amount = 17),
]