from pydantic import BaseModel
from typing import UUID
from enum import Enum

class Genre(str, Enum):
    action = "action"
    adventure = "adventure"
    fantasy = "fantasy"
    mystery = "mystery"
    romance = "romance"
    sci_fi = "Sci-Fi"


class Book(BaseModel):
    id: int
    name: str
    genre: Genre
    author_name: str

    