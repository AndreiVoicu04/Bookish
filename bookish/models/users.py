from bookish.app import db

class Users(db.Model):

    __tablename__ = 'Users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(), unique=True, nullable=False)
    user_password = db.Column(db.String(), nullable=False)

    # relations
   # checked_out_books = db.relationship('Checked_Out_Books', backref='Users', uselist=False)

    def __init__(self, user_name, user_password):
        self.user_name = user_name
        self.user_password = user_password

    def __repr__(self):
        return f"{self.user_id}: {self.user_name}"

    def serialize(self):
        return {
            'user_id': self.user_id,
            'user_name': self.user_name,
            'user_password': self.user_password
        }
