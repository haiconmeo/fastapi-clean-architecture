
from fastapi import APIRouter, Depends
from app.common.db import get_db
from app.modules.auth.business import AuthBiz
from app.modules.auth.model import UserLogin
from app.modules.auth.storage import AuthStorage
from sqlalchemy.orm import Session


class AuthTransport():
    def __init__(self, store: AuthStorage) -> None:
        self.router = APIRouter()
        self.store = store
        self.biz = AuthBiz(store=store)

    def configure_routes(self):
        @self.router.post("/login")
        def login(userLogin: UserLogin, db_: Session = Depends(get_db)):
            return self.biz.authenticate(db=db_, userLogin=userLogin)

    def get_router(self):
        return self.router


store = AuthStorage()
auth_router = AuthTransport(store)
auth_router.configure_routes()
