
from typing import Generic
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.common.db import get_db
from .parameters import common_filter_parameters
from .base_storage import BaseStore, CreateSchemaType, UpdateSchemaType
from .base_business import BaseBiz

router = APIRouter()
class BaseTransport():
    def __init__(self,store: BaseStore) -> None:
        self.router = APIRouter()
        self.store = store
        self.biz = BaseBiz(storage=store) 

    def configure_routes(self,CreateSchemaType, UpdateSchemaType):    
        @self.router.get("")
        def get_list(db_: Session = Depends(get_db),filter_param: str = Depends(common_filter_parameters),):
            return self.biz.get_multi(db=db_,filter_param=filter_param)

        @self.router.post("")
        def create(obj_in:CreateSchemaType,db_: Session = Depends(get_db)):
            return self.biz.create(db=db_,obj_in=obj_in)

        @self.router.get("/{id}")
        def get_one(id:int,db_: Session = Depends(get_db),):
            return self.biz.get(db=db_,id=id)

        @self.router.put("/{id}")
        def update(id:int,obj_in: UpdateSchemaType,db_: Session = Depends(get_db),):
            db_obj = self.biz.get(id)
            return self.biz.update(db=db_,db_obj=db_obj,obj_in=obj_in)

        @self.router.delete("/{id}")
        def delete( id: int,db_: Session = Depends(get_db),):
            return self.biz.remove(db=db_,id=id)

