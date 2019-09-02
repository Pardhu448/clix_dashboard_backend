from functools import wraps
from flask import request, g, abort
from jwt import decode, exceptions
import json
from app import app

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        authorization = request.headers.get("Authorization", None)
        if not authorization:
            return json.dumps({'error': 'no authorization token provied'}), 403, {'Content-type': 'application/json'}

        try:
            token = authorization
            resp = decode(token, app.config.get('SECRET_KEY'), algorithm='HS256')
            g.user = resp['sub']
        except exceptions.DecodeError as identifier:
            return json.dumps({'error': 'invalid authorization token'}), 403, {'Content-type': 'application/json'}

        return f(*args, **kwargs)

    return wrap