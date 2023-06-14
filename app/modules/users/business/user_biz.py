
from app.common.base_business import BaseBiz
from app.modules.users.storage import UserStore


class UserBiz(BaseBiz):
    def __init__(self, storage: UserStore):
        self.storage = storage
        super.__init__(storage)
