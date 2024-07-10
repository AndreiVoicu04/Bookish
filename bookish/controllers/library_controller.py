from flask import request
from bookish.models.example import Example
from bookish.models.books import Books
from bookish.models.users import Users
from bookish.models.checked_out_books import Checked_Out_Books
from bookish.models import db
from bookish.Services.library_handling_services import add_book,borrow_book
import werkzeug


def library_routes(app):
    @app.route('/library/add_book', methods=['POST'])
    def handle_add_book():
        try:
            data = request.get_json()
        except Exception as e:
            raise werkzeug.exceptions.BadRequest("Body must be JSON")
        auth_token = data['auth_token']
        check_if_authenticated(auth_token)

        return add_book(data)

    @app.route('/library/borrow', methods=['POST'])
    def handle_borrow():
        try:
            data = request.get_json()
        except Exception as e:
            raise werkzeug.exceptions.BadRequest("Body must be JSON")
        auth_token = data['auth_token']
        check_if_authenticated(auth_token)
        return borrow_book(data)


