from flask import request
from bookish.Services.user_handling_services import user_signin, user_signup, user_signout
from bookish.models.example import Example
from bookish.models.books import Books
from bookish.models.users import Users
from bookish.models.checked_out_books import Checked_Out_Books
import werkzeug

def login_routes(app):
    @app.route('/login/healthcheck')
    def health_check():
        return {"status": "OK"}

    @app.route('/login/signin', methods=['GET'])
    def handle_signin():
        try:
            data = request.get_json()
        except Exception as e:
            raise werkzeug.exceptions.BadRequest("Body must be JSON")
        return user_signin(data['user_name'], data['user_password'])

    @app.route('/login/signup', methods=['POST'])
    def handle_signup():
        try:
            data = request.get_json()
        except Exception as e:
            raise werkzeug.exceptions.BadRequest("Body must be JSON")

        return user_signup(data['user_name'], data['user_password'])

    @app.route('/login/signout', methods=['GET'])
    def handle_signout():
        try:
            data = request.get_json()
        except Exception as e:
            raise werkzeug.exceptions.BadRequest("Body must be JSON")

        return user_signout(data['auth_token'])
