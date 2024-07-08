import hashlib
from bookish.models.users import Users


def hashing_algorithm(string):
    result = hashlib.md5(string.encode('utf-8')).hexdigest()
    return result


def check_auth_token(token):
    """
    :param token:
    :return: true -> token valid
             false -> token expired/invalid
    """

    all_users = Users.query.all()
    for user in all_users:
        print(user)
        if user.user_token == token and user.user_token_expire > datetime.datetime.now():
            return True
    return False
