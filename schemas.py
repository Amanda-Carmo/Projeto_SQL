from pydantic import BaseModel
from enum import Enum
import uuid
from sqlmodel import Field
import datetime
from typing import Union, Optional, List

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
    # id: int
    book_name: str
    genre: Genre
    author_name: str
    price: float
    amount: int

class BookCreate(BaseModel):
    book_name: str
    genre: Genre
    author_name: str
    price: float

# Para o update request: atributos que se pode atualizar. Não se pode mudar id.
class BookUpdate(BaseModel):
    book_name: Optional[str] = None
    genre: Optional[Genre] = None
    author_name: Optional[str] = None
    price: float
    amount: Optional[int] = None


class OrderCreate(BaseModel):
    user_id: int
    book_name: str
    amount:int
    order_date: datetime.date

# Controle Venda
class Order(BaseModel):
    id: int
    user_id: int
    book_name: str
    amount: int
    order_date: datetime.date


class PurchaseCreate(BaseModel):
    user_id: int

# Controle Compra
class Purchase(BaseModel):
    id: int
    user_id: int
    book_name: str
    amount: int
    purchase_date: datetime.date