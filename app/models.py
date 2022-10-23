from pydantic import BaseModel
from typing import Union
from enum import Enum
from uuid import uuid4
from uuid import UUID 

class Genre(str, Enum):
    action = "action"
    adventure = "adventure"
    fantasy = "fantasy"
    mystery = "mystery"
    sci_fi = "Sci-Fi"
    drama = "drama"


class Book(BaseModel):
    id: UUID = uuid4()
    name: str
    genre: Genre
    author_name: str
    price: float


class BookRequest(BaseModel):
    name: str
    genre: Genre
    author_name: str
    price: float