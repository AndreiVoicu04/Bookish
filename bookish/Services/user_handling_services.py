from bookish.models.users import Users
from bookish.models import db
from bookish.Services.auxiliary_functions import hashing_algorithm


def user_signin(user_name, user_password):
    try:
        all_users = Users.query.all()
    except Exception as e:
        return {"status": "Error", "error_message": str(e), "user_friendly": "Could not query the database"}

    hashed_password = hashing_algorithm(user_password)
    current_user = next(user for user in all_users if user.user_name == user_name)

    if current_user is None:
        return {"status": "Error", "error_message": "Couldn't find the user", "user_friendly": "Couldn't find the user" }
    if current_user.user_password == hashed_password:
        try:
            current_user.create_token()
            db.session.commit()
            return {"status": "Ok", "user_token": {"user_name": current_user.user_name, "user_token": current_user.user_token},
                    "Http_Code": "200"}
        except Exception as e:
            return {"status": "Error", "error_message": str(e), "user_friendly": "Login error"}
    else:
        return {"status": "Error", "error_message": "Incorrect password", "user_friendly": "Incorrect password"}


def user_signup(user_name, user_password):
    user_password = hashing_algorithm(user_password)
    new_user = Users(user_name, user_password)
    try:
        db.session.add(new_user)
        db.session.commit()
        return {"status": "Ok", "user_friendly": "User created successfully", "Http_Code": "200"}
    except Exception as e:
        return {"status": "Error", "error_message": str(e), "user_friendly": "The user could not be created"}


def user_signout(auth_token):
    try:
        all_users = Users.query.all()
    except Exception as e:
        return {"status": "Error", "error_message": str(e), "user_friendly": "Could not query the database"}

    user_name = auth_token["user_name"]
    token = auth_token["user_token"]
    current_user = next(user for user in all_users if user.user_name == user_name)

    if current_user is None:
        return {"status": "Error", "error_message": "Couldn't find the user", "user_friendly": "Couldn't find the user" }
    if current_user.user_token == token:
        try:
            current_user.user_token = None
            current_user.user_token_expire = None
            db.session.commit()
            return {"status": "Ok", "Http_Code": "200", "user_friendly": "User has been signed out."}
        except Exception as e:
            return {"status": "Error", "error_message": str(e), "user_friendly": "Could not sign out"}
    else:
        return {"status": "Error", "error_message": "Token error", "user_friendly": "Token error" }
