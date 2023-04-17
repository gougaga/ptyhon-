from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
class StuModel(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(8), unique=True)
    user_pw = db.Column(db.String(12), unique=True)
    user_name = db.Column(db.String(8), unique=True)
    user_fullname = db.Column(db.String(6), unique=True)
    def __str__(self):
        return self.user_name