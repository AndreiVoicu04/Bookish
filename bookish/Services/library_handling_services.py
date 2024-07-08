from bookish.models import db
from bookish.models.users import Users
from bookish.models.books import Books
from bookish.Services.auxiliary_functions import check_auth_token


def add_book(data):
    auth_token = data['auth_token']
    try:
        is_authenticated = check_auth_token(auth_token)
        if not is_authenticated:
            return {"status": "Error", "error_message": "Not authenticated"}
    except Exception as e:
        return {"status": "Error", "error_message": str(e)}
    book = Books(book_title=data['book_title'], book_author=data['book_author'],
                 book_ISBN=data['book_ISBN'], book_no=data['book_no'], book_available=data['book_available'])

    try:
        db.session.add(book)
        db.session.commit()
        return {"status": "Ok", "message": "Book added successfully"}
    except Exception as e:
        return {"status": "Error", "error_message": str(e)}
