from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.common.base_entity import BaseEntity


class Product(BaseEntity):
    pass