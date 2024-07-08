from bookish.app import db

class Books(db.Model):
    __tablename__ = 'Books'

    book_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_title = db.Column(db.String(255))
    book_author = db.Column(db.String(255))
    book_ISBN = db.Column(db.String(255))
    book_no = db.Column(db.Integer)
    book_available = db.Column(db.Integer)

    # relations
    checked_out_books = db.relationship('Checked_Out_Books', backref='Books', uselist=False)

    def __init__(self, book_title, book_author, book_ISBN, book_no, book_available):
        self.book_title = book_title
        self.book_author = book_author
        self.book_ISBN = book_ISBN
        self.book_no = book_no
        self.book_available = book_available

    def __repr__(self):
        return f"{self.book_id} - {self.book_title} - {self.book_author} - {self.book_ISBN}"

    def serialize(self):
        return {
            'book_id': self.book_id,
            'book_title': self.book_title,
            'book_author': self.book_author,
            'book_ISBN': self.book_ISBN,
            'book_no': self.book_no,
            'book_available': self.book_available
        }
