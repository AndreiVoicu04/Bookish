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
    :param token:
    :return: true -> token valid
             false -> token expired/invalid
    """

    all_users = Users.query.all()
    current_user = next(user for user in all_users if user.user_name == auth_token['user_name'])
    if current_user.user_token == auth_token['user_token']:
        if current_user.user_token_expire > datetime.datetime.now():
            return True
    return False


def check_if_authenticated(auth_token):
    try:
        authenticated_status = check_auth_token(auth_token)
        if not authenticated_status:
            raise Exception('Token expired')
    except Exception as e:
        raise e

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
    order = "ASC"
    if request.args.get("order") is not None:
        order = request.args.get("order")
    limit = -1
    if request.args.get("limit") is not None:
        limit = request.args.get("limit")
    return {"book_author": book_author, "book_title": book_title, "order": order, "limit": limit}