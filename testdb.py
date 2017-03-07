import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'shhhh!!!secret'
db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = 'users'
    users_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    fname = db.Column(db.String(64), unique=True)
    lname = db.Column(db.String(64), unique=True)
##     address = db.relationship('Users', backref='Address')

    def __repr__(self):
        return '<Users %r>' % self.name


class Address(db.Model):
    __tablename__ = 'address'
    addr_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.users_id'))
    address = db.Column(db.String(256), unique=True, index=True)

    def __repr__(self):
        return '<Address %r>' % self.address

