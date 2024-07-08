from flask import request
from bookish.models.example import Example
from bookish.models.books import Books
from bookish.models.users import Users
from bookish.models.checked_out_books import Checked_Out_Books
from bookish.models import db

import hashlib


def hashing_algorithm(string):
    result = hashlib.md5(string.encode('utf-8')).hexdigest()
    return result


def bookish_routes(app):
    @app.route('/healthcheck')
    def health_check():
        return {"status": "OK"}

    @app.route('/example', methods=['POST', 'GET'])
    def handle_example():
        if request.method == 'POST':
            if request.is_json:
                data = request.get_json()
                new_example = Example(data1=data['data1'], data2=data['data2'])
                db.session.add(new_example)
                db.session.commit()
                return {"message": "New example has been created successfully."}
            else:
                return {"error": "The request payload is not in JSON format"}

        elif request.method == 'GET':
            examples = Example.query.all()
            results = [
                {
                    'id': example.id,
                    'data1': example.data1,
                    'data2': example.data2
                } for example in examples]
            return {"examples": results}

    @app.route('/signin', methods=['GET'])
    def handle_signin():
        try:
            data = request.get_json()
            all_users = Users.query.all()
            current_user = Users(user_name=data['user_name'], user_password=hashing_algorithm(data['user_password']))
            for user in all_users:
                if user.user_name == current_user.user_name and user.user_password == current_user.user_password:
                    user.create_token()
                    db.session.commit()
                    return {"status": "OK", "user_token" : user.user_token}
            return {"error": "Wrong credentials"}
        except Exception as e:
            return {"error": str(e)}

    @app.route('/showall', methods=['POST', 'GET'])
    def handle_showall():
        try:
            user_name = request.args.get('user_name')
            data = Users.query.all()
            results = [user.serialize() for user in data]
            return results
        except Exception as e:
            return {"error": str(e)}

    @app.route('/signup', methods=['POST'])
    def handle_signup():
        if not request.is_json:
            return {"error": "The request payload is not in JSON format"}
        try:
            data = request.get_json()
            new_user = Users(user_name=data['user_name'], user_password=hashing_algorithm(data['user_password']))
            db.session.add(new_user)
            db.session.commit()
            return {"message": "User has been created successfully."}
        except Exception as e:
            return {"error": str(e)}
