from bookish.models import db
from bookish.models.users import Users
from bookish.models.books import Books
def list_all_users():
    try:
        data = Users.query.all()
    except Exception as e:
        return {"status": "Error", "error_message": str(e)}

    return [user.serialize() for user in data]

def list_all_books():
    try:
        data = Books.query.all()
    except Exception as e:
        return {"status": "Error", "error_message": str(e)}
    return [book.serialize() for book in data]