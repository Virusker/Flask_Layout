from app import db, app

class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

if __name__ == '__main__':
    with app.app_context():
        # db.create_all()
        us = User(username='admin')
        db.session.add(us)
        db.session.commit()
