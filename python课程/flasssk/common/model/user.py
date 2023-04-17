from flask_sqlalchemy import SQLAlchemy  # 导入 SQLALchemy
  # 导入app

db = SQLAlchemy()  # 实例化SQLAlchemy，传入app获得db
class UserModel(db.Model):
    #__tablename__ = 'user'  # 自定义表名
    id = db.Column(db.Integer, primary_key=True)
    u_name = db.Column(db.String(8), unique=True)
    u_pwd = db.Column(db.String(12), unique=True)
    def __str__(self):
        return self.u_name