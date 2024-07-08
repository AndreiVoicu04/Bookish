from bookish.models.users import Users
from bookish.models import db
from bookish.Services.auxiliary_functions import hashing_algorithm

def user_signin(user_name, user_password):
    try:
        all_users = Users.query.all()
    except Exception as e:
        return {"status": "Error", "error_message": str(e)}
    hashed_password = hashing_algorithm(user_password)
    print(hashed_password)
    current_user = Users(user_name=user_name, user_password=hashed_password)
    for user in all_users:
        if user.user_name == user_name and user.user_password == current_user.user_password:
            try:
                user.create_token()
                db.session.commit()
                return {"status": "Ok", "user_token": user.user_token, "Http_Code": "200"}
            except Exception as e:
                return {"status": "Error", "error_message": str(e)}


def user_signup(user_name, user_password):
    user_password = hashing_algorithm(user_password)
    new_user = Users(user_name, user_password)
    try:
        db.session.add(new_user)
        db.session.commit()
        return {"status": "Ok", "message": "User created successfully", "Http_Code": "200"}
    except Exception as e:
        return {"status": "Error", "error_message": str(e)}

