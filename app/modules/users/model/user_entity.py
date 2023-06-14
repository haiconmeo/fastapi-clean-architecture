from sqlalchemy import Column, String
from sqlalchemy.orm import deferred,relationship
from app.common.base_entity import BaseEntity


class Users(BaseEntity):
    full_name = Column(String)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String)
    username = Column(String)
    password = deferred(Column(String))
    items = relationship("Item", back_populates="owner")

