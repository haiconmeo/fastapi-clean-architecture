from typing import Any, List, Literal, Optional
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime

from app.helper.string_case import to_camel_case


class UserBase(BaseModel):
    email: Optional[str] = None
    full_name: Optional[str] = None

    class Config:
        orm_mode = True
        alias_generator = to_camel_case
        allow_population_by_field_name = True


# Properties to receive via API on creation
class Register(UserBase):
    email: str
    password: str


class UserCreate(UserBase):
    email: str
    password: str
    role: Literal["Customer", "Admin", "Editor"]


class UserLogin(BaseModel):
    email: str
    password: str


class UserChangePassword(BaseModel):
    old_password: str
    new_password: str

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True


class UserUpdate(BaseModel):
    email: Optional[str]
    full_name: Optional[str]
    is_active: Optional[bool]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True


class UserInDBBase(UserBase):
    id: Optional[int] = None
    role: Literal["Customer", "Admin", "Editor"]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
        alias_generator = to_camel_case
        allow_population_by_field_name = True


# Additional properties to return via API
class UserSchema(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    password: str
