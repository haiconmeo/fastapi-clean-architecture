
from typing import Generator
from .session import SessionLocal
from typing import Generator
import json
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt
from pydantic import ValidationError
from app.component import TokenPayload

from app.config import security
from app.config import settings


reusable_oauth2 = HTTPBearer(
    scheme_name='Authorization'
)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_user(
    http_authorization_credentials: str = Depends(reusable_oauth2)
):
    try:
        payload = jwt.decode(
            http_authorization_credentials.credentials, settings.SECRET_KEY, algorithms=[
                security.ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        print(f'________in deps______: error {ValidationError}')
        raise HTTPException(  # pylint: disable=raise-missing-from
            status_code=403,
            name="Could not validate credentials",
        )
    user_token = json.loads(token_data.sub)
    return user_token


def get_current_active_superuser(
    current_user=Depends(get_current_user),
):
    if current_user.role != 'Admin':
        raise HTTPException(
            status_code=400, name="The user doesn't have enough privileges"
        )
    return current_user
