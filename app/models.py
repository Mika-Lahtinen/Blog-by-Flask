from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class Role(db.Model):
    __tablename__ = 'roles'
    table_id = db.Column(db.Integer, primary_key=True)
    table_name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.table_name

    users = db.relationship('User', backref='role', lazy='dynamic')


class User(db.Model):
    __tablename__ = 'users'
    table_id = db.Column(db.Integer, primary_key=True)
    table_username = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return '<User %r>' % self.table_username

    role_id = db.Column(db.Integer, db.ForeignKey('roles.table_id'))

    '''
    Add password hashes
    '''
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
