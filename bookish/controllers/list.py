from flask import request, jsonify
from bookish.models.example import Example
from bookish.models.books import Books
from bookish.models.users import Users
from bookish.models.checked_out_books import Checked_Out_Books
from bookish.Services.list_services import list_all_users, list_all_books, list_books_by_author, list_books_by_title, placeholder


def list_routes(app):
    @app.route('/list/users', methods=['GET'])
    def handle_show_all_users():
        all_users = list_all_users()
        return jsonify([user.serialize() for user in all_users])

    @app.route('/list/books', methods=['GET'])
    def handle_show_all_books():
        all_books = list_all_books()
        order = "ASC"
        if request.args.get("order") is not None:
            order = request.args.get("order")
        limit = -1
        if request.args.get("limit") is not None:
            limit = request.args.get("limit")
        all_books = placeholder(all_books, order, limit)
        return jsonify([book.serialize() for book in all_books])

    @app.route('/list/books_by_title', methods=['GET'])
    def handle_show_books_by_title():
        requested_title = request.args.get('book_title')
        if requested_title is None:
            return {"status": "Error", "error_message": "Book title not present", "user_friendly": "Book title not present"}
        order = "ASC"
        if request.args.get("order") is not None:
            order = request.args.get("order")
        limit = -1
        if request.args.get("limit") is not None:
            limit = request.args.get("limit")

        try:
            data = request.get_json()
        except Exception as e:
            return {"status": "Error", "error_message": str(e), "user_friendly": "Body must be JSON"}

        books_by_title = list_books_by_title(data['auth_token'], requested_title)
        books_by_title = placeholder(books_by_title, order, limit)
        return jsonify([book.serialize() for book in books_by_title])

    @app.route('/list/books_by_author', methods=['GET'])
    def handle_show_books_by_author():
        requested_author = request.args.get('book_author')
        if requested_author is None:
            return {"status": "Error", "error_message": "Book author not present", "user_friendly": "Book author not present"}
        order = "ASC"
        if request.args.get("order") is not None:
            order = request.args.get("order")
        limit = -1
        if request.args.get("limit") is not None:
            limit = request.args.get("limit")
        try:
            data = request.get_json()
        except Exception as e:
            return {"status": "Error", "error_message": str(e), "user_friendly": "Body must be JSON"}
        books_by_author = list_books_by_author(data['auth_token'], requested_author)
        books_by_author = placeholder(books_by_author, order, limit)
        return jsonify([book.serialize() for book in books_by_author])
