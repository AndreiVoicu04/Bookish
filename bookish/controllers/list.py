from flask import request
from bookish.models.example import Example
from bookish.models.books import Books
from bookish.models.users import Users
from bookish.models.checked_out_books import Checked_Out_Books
from bookish.Services.list_services import list_all_users, list_all_books, list_books_by_author, list_books_by_title


def list_routes(app):
    @app.route('/list/users', methods=['GET'])
    def handle_show_all_users():
        return list_all_users()

    @app.route('/list/books', methods=['GET'])
    def handle_show_all_books():
        return list_all_books()

    @app.route('/list/books_by_title', methods=['GET'])
    def handle_show_books_by_title():
        try:
            requested_title = request.args.get('book_title')
        except Exception as e:
            return {"status": "Error", "error_message": str(e), "UI_message": "book title not present"}

        try:
            data = request.get_json()
        except Exception as e:
            return {"status": "Error", "error_message": str(e), "UI_message": "Body must be JSON"}

        return list_books_by_title(data['auth_token'], requested_title)

    @app.route('/list/books_by_author', methods=['GET'])
    def handle_show_books_by_author():
        try:
            requested_author = request.args.get('book_author')
        except Exception as e:
            return {"status": "Error", "error_message": str(e), "UI_message": "book author not present"}

        try:
            data = request.get_json()
        except Exception as e:
            return {"status": "Error", "error_message": str(e), "UI_message": "Body must be JSON"}

        return list_books_by_author(data['auth_token'], requested_author)
