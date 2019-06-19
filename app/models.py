from . import db


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
