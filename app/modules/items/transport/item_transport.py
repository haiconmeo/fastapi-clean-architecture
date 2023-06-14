
from app.common.base_transport import BaseTransport
from app.modules.items.storage.item_storage import ItemStore
from app.modules.items.model import ItemCreate,ItemUpdate,Item

class ItemTransport(BaseTransport):
    def __init__(self) -> None:
        self.store = ItemStore(Item)
        super().__init__(self.store)

    def get_router(self):
        return self.router


item_transport = ItemTransport()
item_transport.configure_routes(ItemCreate,ItemUpdate)