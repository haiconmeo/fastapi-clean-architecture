from app.common.base_business import BaseBiz
from app.modules.products.storage import ProductStore


class ProductBiz(BaseBiz):
    def __init__(self,storage: ProductStore):
        self.storage = storage
        super.__init__(storage)