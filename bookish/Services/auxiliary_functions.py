import hashlib
import datetime
from flask import request
from bookish.models.users import Users
from bookish.models.books import Books
from bookish.models.checked_out_books import Checked_Out_Books
from werkzeug.exceptions import HTTPException
from bookish.error_handler import *

def hashing_algorithm(string):
    return hashlib.md5(string.encode('utf-8')).hexdigest()

def date_format(string):
    date_fmt = '%a, %d %b %Y %H:%M:%S %Z'
    return datetime.datetime.strptime(string, date_fmt)

def check_auth_token(auth_token):
    """
    :param auth_token:
    :return: true -> token valid
             false -> token expired/invalid
    """

    current_user = return_user_by_user_name(auth_token['user_name'])
    if current_user is not None and current_user.user_token == auth_token['user_token']:
        if current_user.user_token_expire > datetime.datetime.now():
            return True
    return False


def check_if_authenticated(auth_token):
    try:
        authenticated_status = check_auth_token(auth_token)
        if not authenticated_status:
            raise werkzeug.exceptions.BadRequest("User not authenticated")
    except Exception as e:
        raise werkzeug.exceptions.BadRequest(str(e))

def return_user_by_user_name(user_name):
    all_users = Users.query.all()
    return next((user for user in all_users if user.user_name == user_name), None)

def return_user_by_user_id(user_id):
    all_users = Users.query.all()
    return next((user for user in all_users if user.user_id == user_id), None)

def return_book_by_ISBN(book_ISBN):
    all_books = Books.query.all()
    return next((book for book in all_books if book.book_ISBN == book_ISBN), None)

def request_parser(request):
    book_author = request.args.get('book_author')
    book_title = request.args.get('book_title')
    order = request.args.get("order", default= "ASC")
    limit = request.args.get("limit", default= -1)
    return {"book_author": book_author, "book_title": book_title, "order": order, "limit": limit}