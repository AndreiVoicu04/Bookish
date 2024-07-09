from bookish.models import db
from bookish.models.users import Users
from bookish.models.books import Books


def list_all_users():
    try:
        all_users = Users.query.all()
    except Exception as e:
        return {"status": "Error", "error_message": str(e)}

    return all_users


def list_all_books():
    try:
        all_books = Books.query.all()
    except Exception as e:
        return {"status": "Error", "error_message": str(e)}
    return all_books


def list_books_by_title(auth_token, book_title):
    try:
        check_if_authenticated(auth_token)
    except Exception as e:
        return e

    try:
        all_books_by_title = Books.query.all()
    except Exception as e:
        return {"status": "Error", "error_message": str(e)}

    return all_books_by_title


def list_books_by_author(auth_token, book_author):
    try:
        check_if_authenticated(auth_token)
    except Exception as e:
        return e

    try:
        all_books_by_author = Books.query.all()
    except Exception as e:
        return {"status": "Error", "error_message": str(e)}
    return all_books_by_author

def placeholder(books, order, limit):
    if order == 'ASC':
        books = sorted(books, key=lambda book: book.book_title)
    else:
        books = sorted(books, key=lambda book: book.book_title, reverse=True)
    if limit == -1:
        return books
    return books[:limit]
