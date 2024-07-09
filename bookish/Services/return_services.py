from bookish.models import db
from bookish.models.users import Users
from bookish.models.books import Books
from bookish.models.checked_out_books import Checked_Out_Books
from bookish.Services.auxiliary_functions import check_if_authenticated, return_book_by_ISBN, return_user_by_user_id
from bookish.error_handler import *


def list_all_users():
    try:
        all_users = Users.query.all()
    except Exception as e:
        raise Exception({"status": "Error", "error_message": str(e)})

    return all_users


def list_all_books(parsed_request):
    try:
        all_books = Books.query.all()
    except Exception as e:
        raise Exception({"status": "Error", "error_message": str(e)})
    all_books = apply_list_filters(all_books,  order, limit)
    return all_books


def list_books_by_title(auth_token, book_title):
    try:
        all_books_by_title = filter(lambda book: book.book_title==parsed_request['book_title'],Books.query.all())
    except Exception as e:
        raise Exception({"status": "Error", "error_message": str(e)})
    books_by_title = apply_list_filters(all_books_by_title, parsed_request['order'], parsed_request['limit'])
    return books_by_title


def list_books_by_author(auth_token, parsed_request : dict):
    try:
        print("here")
        all_books_by_author = filter(lambda book: book.book_author==parsed_request['book_author'],Books.query.all())
    except Exception as e:
        raise Exception({"status": "Error", "error_message": str(e)})

    books_by_author = apply_list_filters(all_books_by_author, parsed_request['order'], parsed_request['limit'])
    return books_by_author

def apply_list_filters(books, order, limit):
    if order == 'ASC':
        books = sorted(books, key=lambda book: book.book_title)
    else:
        books = sorted(books, key=lambda book: book.book_title, reverse=True)
    if limit == -1:
        return books
    return books[:limit]

def list_checked_out_books(auth_token):
    try:
        all_checked_out_books = Checked_Out_Books.query.all()
    except Exception as e:
        raise Exception({"status": "Error", "error_message": str(e)})
    return all_checked_out_books

def get_book_by_ISBN(data):
    if data['book_ISBN'] is None:
        raise Exception({"status": "Error", "error_message": "book ISBN not found"})

    current_book = return_book_by_ISBN(data['book_ISBN'])
    if current_book is None:
        raise Exception({"status": "Error", "error_message": "book ISBN not found"})
    book_exemplaries = []
    book_exemplaries.append(current_book)

    try:
        all_checked_out_books = Checked_Out_Books.query.all()
    except Exception as e:
        raise Exception({"status": "Error", "error_message": str(e)})
    current_book_id = return_book_by_ISBN(data['book_ISBN']).book_id

    given_ISBN_checked_out_books = [book for book in all_checked_out_books if book.book_id == current_book_id]
    print(given_ISBN_checked_out_books)
    for book in given_ISBN_checked_out_books:
        user_id = book.user_id
        user = return_user_by_user_id(user_id)
        checked_out_books = {"user_name": user.user_name, "due_date": book.due_date}
        book_exemplaries.append(checked_out_books)
    print(book_exemplaries)
    return book_exemplaries

