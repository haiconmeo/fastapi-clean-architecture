from typing import Any, Dict, Union
from sqlalchemy.orm import Session

from app.common import base_storage


class BaseBiz:
    def __init__(self,storage: base_storage.BaseStore):
        self.storage = storage

    def get(self,db: Session,id: int):
        return self.storage.get(db,id)
    
    def get_multi(self,db: Session,filter_param: dict = None):
        return self.storage.get_multi(db,filter_param=filter_param)
    
    def create(self, db: Session, obj_in: base_storage.CreateSchemaType):
         return self.storage.create(db=db,obj_in=obj_in)
    
    def update(self,db: Session, db_obj: base_storage.ModelType,
        obj_in: Union[base_storage.UpdateSchemaType, Dict[str, Any]]):
        return self.storage.update(db,db_obj=db_obj,obj_in=obj_in)
    
    def remove(self,db: Session,id:int):
        return self.storage.remove(db,id=id)


