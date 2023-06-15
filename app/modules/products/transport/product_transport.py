
from app.common.base_transport import BaseTransport
from app.modules.products.storage.product_storage import ProductStore
from app.modules.products.model import ProductCreate,ProductUpdate,Product

class ProductTransport(BaseTransport):
    def __init__(self) -> None:
        self.store = ProductStore(Product)
        super().__init__(self.store)

    def get_router(self):
        return self.router


product_transport = ProductTransport()
product_transport.configure_routes(ProductCreate,ProductUpdate)