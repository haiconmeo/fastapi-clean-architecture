
from app.common.base_storage import BaseStore
from app.modules.users.model import Users,UserCreate, UserUpdate

class UserStore(BaseStore[Users,UserCreate,UserUpdate]):
    pass

