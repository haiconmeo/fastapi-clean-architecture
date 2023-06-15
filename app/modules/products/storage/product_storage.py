from app.common.base_storage import BaseStore
from app.modules.products.model import Product,ProductCreate, ProductUpdate

class ProductStore(BaseStore[Product,ProductCreate,ProductUpdate]):
    pass