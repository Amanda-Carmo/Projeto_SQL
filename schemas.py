from pydantic import BaseModel
from enum import Enum
import uuid
from sqlmodel import Field
import datetime
from typing import Union

# Gênero dos livros
class Genre(str, Enum):
    action = "action"
    adventure = "adventure"
    fantasy = "fantasy"
    mystery = "mystery"
    sci_fi = "Sci-Fi"
    drama = "drama"

# Livros
class Book(BaseModel):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        index=True,
        nullable=False,
    )
    name: str
    genre: Genre
    author_name: str
    price: float
    amount: int

# Para o update request: atributos que se pode atualizar. Não se pode mudar id.
class BookRequest(BaseModel):
    name: str
    genre: Genre
    author_name: str
    price: float
    amount: int

class OrderCreate(BaseModel):
    user_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        index=True,
        nullable=False,
    )

# Controle Venda
class Order(BaseModel):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        index=True,
        nullable=False,
    )
    book_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        index=True,
        nullable=False,
    )
    amount: int
    order_date: datetime.date


class PurchaseCreate(BaseModel):
    user_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        index=True,
        nullable=False,
    )

# Controle Compra
class Purchase(BaseModel):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        index=True,
        nullable=False,
    )
    book_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        index=True,
        nullable=False,
    )
    amount: int
    purchase_date: datetime.date