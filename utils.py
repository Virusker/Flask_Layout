from models import User
from app import app, db

def findd(username):
    return User.query.filter_by(username=username).first()

def add(username):
    user = User(username=username)
    db.session.add(user)
    db.session.commit()
    return user

def get_all():
    return User.query.all()