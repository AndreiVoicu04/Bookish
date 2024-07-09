from flask import request, jsonify
from bookish.models.example import Example
from bookish.models.books import Books
from bookish.models.users import Users
from bookish.models.checked_out_books import Checked_Out_Books
from bookish.Services.list_services import (list_all_users, list_all_books, list_books_by_author, list_books_by_title,
                                            apply_list_filters, list_checked_out_books, get_book_by_ISBN)
from bookish.Services.auxiliary_functions import request_parser


def list_routes(app):
    @app.route('/list/users', methods=['GET'])
    def handle_show_all_users():
        try:
            all_users = list_all_users()
            return jsonify([user.serialize() for user in all_users])
        except Exception as e:
            return str(e)

    @app.route('/list/books', methods=['GET'])
    def handle_show_all_books():
        try:
            parsed_requests = request_parser(request)
            all_books = list_all_books(parsed_requests)
            return jsonify([book.serialize() for book in all_books])
        except Exception as e:
            return str(e)

    @app.route('/list/book', methods=['GET'])
    def handle_show_book():
        try:
            data = request.get_json()
        except Exception as e:
            return {"status": "Error", "error_message": str(e), "user_friendly": "Body must be JSON"}

        book_exemplaries = get_book_by_ISBN(data)

        return jsonify([book.serialize() if isinstance(book, Books) else book for book in book_exemplaries])



    @app.route('/list/books_by_title', methods=['GET'])
    def handle_show_books_by_title():
        parsed_request = request_parser(request)
        if parsed_request['book_title'] is None:
            return {"status": "Error", "error_message": "Book title not present", "user_friendly": "Book title not present"}
        try:
            data = request.get_json()
        except Exception as e:
            return {"status": "Error", "error_message": str(e), "user_friendly": "Body must be JSON"}
        try:
            books_by_title = list_books_by_title(data['auth_token'], parsed_request)
            return jsonify([book.serialize() for book in books_by_title])
        except Exception as e:
            return str(e)

    @app.route('/list/books_by_author', methods=['GET'])
    def handle_show_books_by_author():
        parsed_request = request_parser(request)

        if parsed_request['book_author'] is None:
            return {"status": "Error", "error_message": "Book author not present", "user_friendly": "Book author not present"}
        try:
            data = request.get_json()
        except Exception as e:
            return {"status": "Error", "error_message": str(e), "user_friendly": "Body must be JSON"}
        try:
            books_by_author = list_books_by_author(data['auth_token'], parsed_request)
            return jsonify([book.serialize() for book in books_by_author])
        except Exception as e:
            return str(e)

    @app.route('/list/checked_out_books', methods=['GET'])
    def handle_show_checked_out_books():
        try:
            data = request.get_json()
        except Exception as e:
            return {"status": "Error", "error_message": str(e), "user_friendly": "Body must be JSON"}
        try:
            checked_out_books = list_checked_out_books(data['auth_token'])
            return jsonify([book.serialize() for book in checked_out_books])
        except Exception as e:
            return str(e)
