
from sqlalchemy.orm import Session
from typing import Optional

from app.modules.users.model import Users


class AuthStorage:
    def get_by_email(self, db: Session, email: str) -> Optional[Users]:
        return db.query(Users).filter(Users.email == email).first()
