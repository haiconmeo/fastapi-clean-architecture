from fastapi import APIRouter
from app.modules.users import user_transport
from app.modules.items import item_transport
from app.modules.auth import auth_router

api_router = APIRouter()

api_router.include_router(auth_router.get_router(),
                          prefix="/auth", tags=["auth"])
api_router.include_router(user_transport.get_router(),
                          prefix="/users", tags=["users"])
api_router.include_router(item_transport.get_router(),
                          prefix="/items", tags=["items"])
from app.modules.products import product_transport
api_router.include_router(product_transport.get_router(),prefix="/products", tags=["products"])
