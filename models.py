from pydantic import BaseModel
from typing import Union
from enum import Enum
import uuid
from sqlmodel import Field

class Genre(str, Enum):
    action = "action"
    adventure = "adventure"
    fantasy = "fantasy"
    mystery = "mystery"
    sci_fi = "Sci-Fi"
    drama = "drama"


class Book(BaseModel):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    name: str
    genre: Genre
    author_name: str
    price: float


class BookRequest(BaseModel):
    name: str
    genre: Genre
    author_name: str
    price: float