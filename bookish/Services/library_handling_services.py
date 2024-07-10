from bookish.models import db
from bookish.models.users import Users
from bookish.models.books import Books
from bookish.models.checked_out_books import Checked_Out_Books
from bookish.Services.auxiliary_functions import check_if_authenticated, return_user_by_user_name, return_book_by_ISBN, date_format
import datetime



def add_book(data):
    book = Books(book_title=data['book_title'], book_author=data['book_author'],
                 book_ISBN=data['book_ISBN'], book_no=data['book_no'], book_available=data['book_available'])

    try:
        db.session.add(book)
        db.session.commit()
        return {"status": "Ok", "message": "Book added successfully"}
    except Exception as e:
        return {"status": "Error", "error_message": str(e), "user_friendly": "The book could not be added"}

def borrow_book(data):

    current_user = return_user_by_user_name(auth_token['user_name'])

    current_book = return_book_by_ISBN(data['book_ISBN'])
    if current_book is None:
        return {"status": "Error", "error_message": "The book does not exist", "user_friendly": "The book does not exist"}
    if current_book.book_available <= 0:
        return {"status": "Error", "error_message": "Not enough books", "user_friendly": "Not enough books"}

    if data['due_date'] is None:
            return {"status": "Error", "error_message": "Invalid due date", "user_friendly": "Invalid due date"}
    due_date = date_format(data['due_date']).date()
    if due_date < datetime.date.today():
        return {"status": "Error", "error_message": "Invalid due date", "user_friendly": "Invalid due date"}
    borrowed_book = Checked_Out_Books(user_id=current_user.user_id, book_id=current_book.book_id, due_date=data['due_date'])
    current_book.book_available -= 1
    try:
        db.session.add(borrowed_book)
        db.session.commit()
        return {"status": "Ok", "message": "Book borrowed successfully"}
    except Exception as e:
        return {"status": "Error", "error_message": str(e), "user_friendly": "Database connection error"}


