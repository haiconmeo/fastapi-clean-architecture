
from typing import Optional
from pydantic import BaseModel
from app.helper.string_case import to_camel_case


class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True


class TokenPayload(BaseModel):
    sub: Optional[str] = None
