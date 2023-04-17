from flask_sqlalchemy import SQLAlchemy  # 导入 SQLALchemy
  # 导入app

db = SQLAlchemy()  # 实例化SQLAlchemy，传入app获得db
class UserModel(db.Model):
    tablename__ = 'student'  # 自定义表名
    u_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(80), unique=True)
    u_name = db.Column(db.String(120))
    u_pwd = db.Column(db.String(80))
    user_fullname = db.Column(db.String(10))
    def __str__(self):
        return self.u_name