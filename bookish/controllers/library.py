from flask import request
from bookish.models.example import Example
from bookish.models.books import Books
from bookish.models.users import Users
from bookish.models.checked_out_books import Checked_Out_Books
from bookish.models import db
from bookish.Services.library_handling_services import add_book,borrow_book



def library_routes(app):
    @app.route('/library/add_book', methods=['POST'])
    def handle_add_book():
        try:
            data = request.get_json()
        except Exception as e:
            return {"status": "Error", "error_message": str(e), "user_friendly": "Body must be JSON"}

        return add_book(data)

    @app.route('/library/borrow', methods=['POST'])
    def handle_borrow():
        try:
            data = request.get_json()
        except Exception as e:
            return {"status": "Error", "error_message": str(e), "user_friendly": "Body must be JSON"}
        return borrow_book(data)


