from flask import Flask
from settings import DevelopmentConfig
# 导入蓝图
from apps.student.views import address_bp
from flask_restful import Api, Resource
from apps.teacher.xh import teacher_bp
from apps.student.user import user_bp
from apps.student.stu import aitwo_bp
from common.model.user import db
def create_flask_app(config):
    # 创建对象
    app = Flask(__name__)
    # 加载配置
    app.config.from_object(config)
    # 返回app
    return app

# 调用工厂方法
app = create_flask_app(DevelopmentConfig)

# 注册蓝图
#app.register_blueprint(address_bp)
#api = Api(app)
'''
1.导入Api与Resource，api用于创建api对象v，Resource用于类似视图的形式实现
2.创建api对象
3.自定义视图类型，必须继承Resource
4.视图类中定义请求方法
5.使用api对象添加路由
'''
#class IndexResource(Resource):
    #def get(self):
        #return 'First Restful'
#api.add_resource(IndexResource, '/', endpoint='first')

# 初始化整个项目的db
db.init_app(app)

app.register_blueprint(user_bp)
app.register_blueprint(teacher_bp)
app.register_blueprint(aitwo_bp)
if __name__ == '__main__':
    app.run()