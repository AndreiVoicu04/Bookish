import hashlib
import datetime
from bookish.models.users import Users


def hashing_algorithm(string):
    return hashlib.md5(string.encode('utf-8')).hexdigest()


def check_auth_token(auth_token: dict):
    """
    :param token:
    :return: true -> token valid
             false -> token expired/invalid
    """

    all_users = Users.query.all()
    current_user = next(user for user in all_users if user.user_name == auth_token['user_name'])
    if current_user.user_token == auth_token['user_token']:
        if current_user.user_token_expire > datetime.datetime.now():
            return True
    return False


def check_if_authenticated(auth_token):
    try:
        authenticated_status = check_auth_token(auth_token)
        if not authenticated_status:
            raise {"status": "Error", "error_message": "Not authenticated", "user_friendly": "Not authenticated"}
    except Exception as e:
        raise {"status": "Error", "error_message": str(e), "user_friendly": "Could not check token"}
    return True