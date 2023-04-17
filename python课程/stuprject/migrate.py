from flask_migrate import Migrate, MigrateCommand # 导入迁移类和迁移命令类
from flask_script import Shell, Manager # 导入命令类和管理类
from common.model.user import db
from app import app

manager = Manager(app) # 实例化管理者对象
migrate = Migrate(app, db) # 实例化迁移对象
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()