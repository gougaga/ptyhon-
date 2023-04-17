from flask import Flask
# from common.model.user import db
from settings import DevelopmentConfig, DefaultConfig

from flask_restful import Api,Resource

from common.model.user import db
from flask_cors import CORS
from apps.stu import stu_db
app = Flask(__name__)
def create_flask_app(config):
    # 1.创建对象
    #app = Flask(__name__)
    # 2.加载配置
    app.config.from_object(config)
    db.init_app(app)
    cors = CORS(app)
    #cors.init_app(app, supports_credentials=True)
    app.register_blueprint(stu_db)
    return app

app = create_flask_app(DevelopmentConfig)
# api = Api(app)
# @app.route('/')
# def hello_world():
#     return 'Hello World!'

#db.init_app(app)
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3001)
