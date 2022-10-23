from uuid import uuid4
from pydantic import BaseModel
from typing import UUID, uuid4
from enum import Enum

class Genre(str, Enum):
    action = "action"
    adventure = "adventure"
    fantasy = "fantasy"
    mystery = "mystery"
    sci_fi = "Sci-Fi"
    drama = "drama"


class Book(BaseModel):
    id: UUID # = uuid4
    name: str
    genre: Genre
    author_name: str