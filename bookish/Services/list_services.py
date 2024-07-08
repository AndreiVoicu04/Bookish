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
        all_books = Books.query.all()
    except Exception as e:
        return {"status": "Error", "error_message": str(e)}
    return sorted([book.serialize() for book in all_books],key=lambda book: book['book_title'])


def list_books_by_title(auth_token, book_title):
    try:
        check_if_authenticated(auth_token)
    except Exception as e:
        return e

    try:
        all_books = Books.query.all()
    except Exception as e:
        return {"status": "Error", "error_message": str(e)}

    return sorted([book.serialize() for book in all_books if book.book_title == book_title], key=lambda book: book['book_title'])


def list_books_by_author(auth_token, book_author):
    try:
        check_if_authenticated(auth_token)
    except Exception as e:
        return e

    try:
        data = Books.query.all()
    except Exception as e:
        return {"status": "Error", "error_message": str(e)}
    return sorted([book.serialize() for book in data if book.book_author == book_author],key=lambda book: book['book_title'])