from bookish.app import db

class Checked_Out_Books(db.Model):
    __tablename__ = 'Checked_Out_Books'

    transaction_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'))
    book_id = db.Column(db.Integer, db.ForeignKey('Books.book_id'))
    due_date = db.Column(db.Date)

    def __init__(self, user_id, book_id, due_date):
        self.user_id = user_id
        self.book_id = book_id
        self.due_date = due_date

    def __repr__(self):
        return f"<Checked_Out_Books {self.book_id} {self.user_id} {self.due_date}>"

    def serialize(self):
        return {
            'transaction_id': self.transaction_id,
            'user_id': self.user_id,
            'book_id': self.book_id,
            'due_date': self.due_date
        }
