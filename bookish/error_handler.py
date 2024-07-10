from flask import jsonify,request,Flask
import json
from werkzeug.exceptions import HTTPException
import werkzeug
def handle_http_exception(e):
    response = e.get_response()
    print(e)
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = 'application/json'
    return response
