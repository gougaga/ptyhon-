from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager
from common.model.user import db
from app import app

manger = Manager(app)
migrate = Migrate(app, db)
manger.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manger.run()