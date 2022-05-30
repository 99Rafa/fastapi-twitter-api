from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class BaseUser(BaseModel):
    user_id: str = Field(
        ...,
        example="875a5138-466f-4954-9986-6864a928bdc7",
    )
    email: EmailStr = Field(
        ...,
        example="rafa@gmail.com",
    )


class UserInfo(BaseModel):
    first_name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="Rafael",
    )
    last_name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="Aguirre",
    )
    birth_date: Optional[date] = Field(
        default=None,
    )


class User(BaseUser, UserInfo):
    pass


class UserCredentials(BaseModel):
    email: EmailStr = Field(
        ...,
        example="rafa@gmail.com",
    )
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        example="123456789",
    )


class UserRegister(UserCredentials, UserInfo):
    pass


class UserUpdate(UserInfo):
    email: EmailStr = Field(
        ...,
        example="rafa@gmail.com",
    )
