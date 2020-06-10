from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login


# Model for the user table
class User(UserMixin, db.Model):
    # Set the table name
    __tablename__ = 'user'

    # Set tables columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    # Function used to print the model
    def __repr__(self):
        return '<User {}>'.format(self.username)

    # Set the password in the database
    def set_password(self, password):
        # Password is hashed and saved as a non-reversible hash value
        # Actual password is only known while handling account creation and connection request
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        # Check if a given password corresponds to the the non-reversible hash-value
        # Actual password is only known while handling account creation and connection request
        return check_password_hash(self.password_hash, password)


# Get a user from ID
@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
