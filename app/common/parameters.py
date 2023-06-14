from app.helper.string_case import convert_filter_to_camel_case
from app.helper.string_case import to_snake_case


async def common_filter_parameters(
    page: int = 1, limit: int = 100, filter: str = '{}', include: str = None,
        orderBy: str = None,
):
    filter_ = convert_filter_to_camel_case(filter)
    if (include):
        include = to_snake_case(include)
    skip = (page - 1) * limit
    if skip < 1:
        skip = 0
    if orderBy:
        orderBy = to_snake_case(orderBy)
    return {'skip': skip, 'limit': limit, 'filter': filter_, 'include': include, 'order_by': orderBy}


async def gitlab_pagination(
    page: int = 1, limit: int = 100, search: str = ''
):
    return {"page": page, 'size': limit, 'search': search}
