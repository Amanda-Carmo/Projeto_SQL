from uuid import UUID, uuid3, uuid4
from pydantic import BaseModel
from typing import Union
from enum import Enum
# from uuidbase62 import con_uuidbase62, UUIDBase62, UUIDBase62ModelMixin, get_validated_uuidbase62_by_model

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