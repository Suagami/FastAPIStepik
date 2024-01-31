from datetime import datetime
from enum import Enum
from typing import List, Union

from pydantic import BaseModel, EmailStr, Field, PositiveInt


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: PositiveInt | None
    is_subscribed: bool | None = None


class Feedback(BaseModel):
    name: str
    message: str


class Product(BaseModel):
    product_id: int
    name: str
    category: str
    price: float


class Role(Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"


class AuthRequest(BaseModel):
    username: str
    password: str


class User(BaseModel):
    username: str
    password: str
    role: Role


class AuthUser(BaseModel):
    username: str
    role: Role
