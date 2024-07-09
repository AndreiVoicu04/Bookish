from flask import jsonify
from werkzeug.exceptions import HTTPException
import werkzeug

class CustomHttpException(HTTPException):
    def __init__(self, e):
        super().__init__()
        self.e = e
def handle_bad_request(e):
    print(e)
    return 'bad xczczxrequest!', 403
