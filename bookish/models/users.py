from bookish.app import db
import datetime
import hashlib
from random import randint
class Users(db.Model):

    __tablename__ = 'Users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(), unique=True, nullable=False)
    user_password = db.Column(db.String(), nullable=False)
    user_token = db.Column(db.String())
    user_token_expire = db.Column(db.DateTime())

    # relations
    checked_out_books = db.relationship('Checked_Out_Books', backref='Users', uselist=False)

    def __init__(self, user_name, user_password):
        self.user_name = user_name
        self.user_password = user_password

    def __repr__(self):
        return f"{self.user_id}: {self.user_name}, {self.user_password}, {self.user_token}, {self.user_token_expire}"

    def serialize(self):
        return {
            'user_id': self.user_id,
            'user_name': self.user_name,
            'user_password': self.user_password,
            'user_token': self.user_token,
            'user_token_expire': self.user_token_expire,
        }

    def create_token(self):
        """

        :return: token
        """
        self.user_token_expire = datetime.datetime.now() + datetime.timedelta(minutes=30)
        string = str(randint(1000, 9999))
        self.user_token = hashlib.md5(string.encode('utf-8')).hexdigest()

        return self.user_token
