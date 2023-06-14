from sqlalchemy.ext.declarative import as_declarative, declared_attr
from re import sub
from sqlalchemy import Column, DateTime, Integer
from datetime import datetime

def snake_case(s):
    return '_'.join(
        sub('([A-Z][a-z]+)', r' \1',
            sub('([A-Z]+)', r' \1',
                s.replace('-', ' '))).split()).lower()


@as_declarative()
class BaseEntity():
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now)
    updated_at = Column(DateTime(timezone=True),
                        default=datetime.now, onupdate=datetime.now)
    deleted_at = Column(DateTime(timezone=True), default=None)

    __name__: str

    # Generate __tablename__ automatically

    @declared_attr
    def __tablename__(cls) -> str:
        return snake_case(cls.__name__)
