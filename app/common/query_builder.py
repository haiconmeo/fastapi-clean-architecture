import json
from sqlalchemy import and_, or_, func
from typing import Type, TypeVar
from sqlalchemy.orm import Session, selectinload
from .base_entity import BaseEntity
from sqlalchemy.sql.expression import cast
import sqlalchemy

ModelType = TypeVar("ModelType", bound=BaseEntity)

# A
# filter={"title__like":"%a%"}
# --->>>   SELECT * FROM items WHERE title like '%a%'

# A and B
# filter={"title__ilike":"%a%", "id__gte":1}
# --->>>   SELECT * FROM items WHERE (title ilike '%a%') AND (id >= 1)

# A and B and C
# filter={"title__like":"%a%", "id__lt":10, "owner_id": 1}
# --->>>   SELECT * FROM items WHERE (title like '%a%') AND (id < 10) AND (owner_id = 1)

# A or B
# filter=[{"title__ilike":"%a%"}, {"id__gte":1}]
# --->>>   SELECT * FROM items WHERE (title ilike '%a%') OR (id >= 1)

# A or B or C
# filter=[{"title__like":"%a%"}, {"id__lt":10}, {"owner_id": 1}]
# --->>>   SELECT * FROM items WHERE (title like '%a%') OR (id < 10) OR (owner_id = 1)

# (A and B) or C
# filter=[{"title__like":"%a%", "id__lt":10}, {"owner_id": 1}]
# --->>>   SELECT * FROM items WHERE (title like '%a%' AND id < 10) OR owner_id = 1

# (A and B and C) or D
# filter=[{"title__like":"%a%", "id__lt":10, "id__gt": 1}, {"owner_id": 1}]
# --->>>   SELECT * FROM items WHERE (title like '%a%' AND id < 10 AND id > 1) OR owner_id = 1

# (A and B) or (C and D)
# filter=[{"title__like":"%a%", "id__lt":10}, {"id__gt": 1, "owner_id": 1}]
# --->>>   SELECT * FROM items WHERE (title like '%a%' AND id < 10) OR (id > 1 AND owner_id = 1)

# (A or B) and C
# filter={"0":[{"title__like":"%a%"}, {"owner_id": 1}], "owner_id__lte": 20}
# --->>>   SELECT * FROM items WHERE (title like '%a%' OR owner_id = 1) AND owner_id <= 20

# (A or B) and (C or D)
# filter={"0":[{"title__like":"%a%"}, {"owner_id": 1}], "1":[{"owner_id__lte": 20}, {"owner_id__gte": 10}]}
# --->>>   SELECT * FROM items WHERE (title like '%a%' OR owner_id = 1) AND (owner_id <= 20 OR owner_id >= 10)


def query_builder(
    db: Session,
    model: Type[ModelType],
    filter: str = None,
    order_by: str = None,
    include: str = None,
    join: Type[ModelType] = None,
):
    if (join):
        query = db.query(model, join)
    else:
        query = db.query(model)

    if filter is not None:
        filter = get_filter(model, json.loads(filter))
        query = query.filter(filter)

    if include is not None:
        include = get_include(include)
        query = query.options(*include)

    if order_by is not None:
        order_by = get_order_by(model, order_by)
        query = query.order_by(*order_by)
    return query


def get_filter(model: Type[ModelType], filters):
    if isinstance(filters, list):
        return or_(*[get_filter(model, filter) for filter in filters])

    if isinstance(filters, dict):
        sub_filters = [value for key, value in filters.items()
                       if key.isnumeric()]
        ops_1 = [get_filter(model, sub_filter) for sub_filter in sub_filters]

        conditions = [cdt for cdt in filters.items() if not cdt[0].isnumeric()]
        ops_2 = [get_op(model, *cdt) for cdt in conditions]

        return and_(*ops_1, *ops_2)


def get_count(query):
    counter = query.statement.with_only_columns([func.count()])
    counter = counter.order_by(None)
    return query.session.execute(counter).scalar()


def get_include(include):
    return [selectinload(rlt) for rlt in include.split(",")]


def get_order_by(model, order_by):
    return [get_attr_order(model, attr) for attr in order_by.split(",")]


def get_attr_order(model, attr):
    if attr.startswith("-"):
        return getattr(model, attr[1:]).desc()
    return getattr(model, attr).asc()


def get_op(model: Type[ModelType], key: str, value: str):
    column = key.split("__")[0]
    op = getattr(model, column) == value
    if key.endswith("__lt"):
        op = getattr(model, column) < value
    if key.endswith("__lte"):
        op = getattr(model, column) <= value
    if key.endswith("__gte"):
        op = getattr(model, column) >= value
    if key.endswith("__gt"):
        op = getattr(model, column) > value
    if key.endswith("__neq"):
        op = getattr(model, column) != value
    if key.endswith("__like"):
        op = cast(getattr(model, column), sqlalchemy.String).like(f'%{value}%')
    if key.endswith("__ilike"):
        op = cast(getattr(model, column),
                  sqlalchemy.String).ilike(f'%{value}%')
    if key.endswith("__in"):
        op = getattr(model, column).in_(value)
    if key.endswith("__nin"):
        op = ~getattr(model, column).in_(value)
    if key.endswith("__is"):
        op = getattr(model, column).is_(value)
    if key.endswith("__isn"):
        op = getattr(model, column).isnot(value)
    return op
