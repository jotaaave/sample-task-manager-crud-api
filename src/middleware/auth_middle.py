from functools import wraps
from flask import request, jsonify, g
import jwt
import os

def auth_require(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return jsonify({
                "error": "Token não enviado"
            }), 401

        try:
            token = auth_header.split(" ")[1]
            payload = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=['HS256'])

            g.user_id = payload["user_id"]
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expirado"})
        except jwt.InvalidTokenError:
            return jsonify({"error": "Token Invalido"})

        return f(*args, **kwargs)
    
    return wrapper