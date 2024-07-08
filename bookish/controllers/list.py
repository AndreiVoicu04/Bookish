from flask import request
from bookish.models.example import Example
from bookish.models.books import Books
from bookish.models.users import Users
from bookish.models.checked_out_books import Checked_Out_Books
from bookish.Services.list_services import list_all_users,list_all_books


def list_routes(app):
    @app.route('/list/users', methods=['GET'])
    def handle_show_all_users():
        return list_all_users()

    @app.route('/list/books', methods=['GET'])
    def handle_show_all_books():
        return list_all_books()
