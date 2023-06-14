
from app.common.base_transport import BaseTransport
from app.modules.users.storage.user_storage import UserStore
from app.modules.users.model import UserCreate, UserUpdate, Users


class UserTransport(BaseTransport):
    def __init__(self) -> None:
        self.store = UserStore(Users)
        super().__init__(self.store)

    def configure_routes(self, UserCreate, UserUpdate):
        @self.router.post("/test")
        def test():
            return "test"
        super().configure_routes(CreateSchemaType=UserCreate, UpdateSchemaType=UserUpdate)

    def get_router(self):
        return self.router


user_transport = UserTransport()
user_transport.configure_routes(UserCreate, UserUpdate)
