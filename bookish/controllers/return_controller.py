from flask import request, jsonify, abort
from bookish.models.example import Example
from bookish.models.books import Books
from bookish.models.users import Users
from bookish.models.checked_out_books import Checked_Out_Books
from bookish.Services.return_services import (return_all_users, return_all_books, return_books_by_author, return_books_by_title,
                                              apply_list_filters, return_checked_out_books, get_book_by_ISBN, check_if_authenticated)
from bookish.Services.auxiliary_functions import request_parser
from bookish.error_handler import *
import werkzeug


"""
Question:
Is the way we handled exception ok? Should we move the
http exception handling logic to the controller and raise
other, more precise exceptions in the service?
"""
def return_routes(app):
    @app.route('/return/users', methods=['GET'])
    def handle_show_all_users():
        all_users = return_all_users()
        return jsonify([user.serialize() for user in all_users])

    @app.route('/return/books', methods=['GET'])
    def handle_show_all_books():
        parsed_requests = request_parser(request)
        all_books = return_all_books(parsed_requests)
        return jsonify([book.serialize() for book in all_books])

    @app.route('/return/book', methods=['GET'])
    def handle_show_book():
        try:
            data = request.get_json()
        except Exception as e:
            raise werkzeug.exceptions.BadRequest("Body must be JSON")
        check_if_authenticated(data['auth_token'])
        try:
            book_exemplaries = get_book_by_ISBN(data)
        except Exception as e:
            raise
        return jsonify([book.serialize() if isinstance(book, Books) else book for book in book_exemplaries])



    @app.route('/return/books_by_title', methods=['GET'])
    def handle_show_books_by_title():
        parsed_request = request_parser(request)
        if parsed_request['book_title'] is None:
            raise werkzeug.exceptions.BadRequest("Book title cannot be empty")
        try:
            data = request.get_json()
        except Exception as e:
            raise werkzeug.exceptions.BadRequest("Body must be JSON")

        check_if_authenticated(auth_token)

        try:
            books_by_title = return_books_by_title(data['auth_token'], parsed_request)
            return jsonify([book.serialize() for book in books_by_title])
        except Exception as e:
            raise werkzeug.exceptions.InternalServerError(str(e))

    @app.route('/return/books_by_author', methods=['GET'])
    def handle_show_books_by_author():
        parsed_request = request_parser(request)

        if parsed_request['book_author'] is None:
            raise werkzeug.exceptions.BadRequest("Book author cannot be empty")
        try:
            data = request.get_json()
        except Exception as e:
            raise werkzeug.exceptions.BadRequest("Body must be JSON")

        check_if_authenticated(auth_token)
        books_by_author = return_books_by_author(data['auth_token'], parsed_request)
        return jsonify([book.serialize() for book in books_by_author])

    @app.route('/return/checked_out_books', methods=['GET'])
    def handle_show_checked_out_books():
        try:
            data = request.get_json()
        except Exception as e:
            raise werkzeug.exceptions.BadRequest("Body must be JSON")

        check_if_authenticated(auth_token)

        try:
            checked_out_books = list_checked_out_books(data['auth_token'])
            return jsonify([book.serialize() for book in checked_out_books])
        except Exception as e:
            raise werkzeug.exceptions.InternalServerError(str(e))
