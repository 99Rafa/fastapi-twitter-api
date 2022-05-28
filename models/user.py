from datetime import date
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


class BaseUser(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)


class User(BaseUser):
    first_name: str = Field(
        ...,
        min_length=3,
        max_length=50,
    )
    last_name: str = Field(
        ...,
        min_length=3,
        max_length=50,
    )
    birth_date: Optional[date] = Field(
        default=None,
    )


class UserLogin(BaseUser):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
    )


class UserRegister(User, UserLogin):
    pass
