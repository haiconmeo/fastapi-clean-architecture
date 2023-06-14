from datetime import timedelta
import json
from app.modules.auth.model import UserLogin
from app.modules.auth.storage import AuthStorage
from app.config import settings, security


class AuthBiz:
    def __init__(self, store: AuthStorage) -> None:
        self.store = store

    def authenticate(self, db, user_login: UserLogin):
        user = self.store.get_by_email(db, user_login.email)
        if not user:
            raise
        if not security.verify_password(user_login.password, user.password):
            return None
        access_token_expires = timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        user_token = {"id": str(user.id)}
        return {
            "access_token": security.create_access_token(
                json.dumps(user_token), expires_delta=access_token_expires
            ),
            "token_type": "bearer",
            "user": user
        }
