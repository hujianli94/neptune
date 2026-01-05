#!/usr/bin/env python
from flask import request
from api.util import jsonify


def paginate(query, schema):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    paginated = query.paginate(page=page, per_page=per_page, error_out=False)

    return jsonify({
        "items": schema.dump(paginated.items),
        "total": paginated.total,
        "pages": paginated.pages,
        "current_page": paginated.page,
        "per_page": paginated.per_page
    })
