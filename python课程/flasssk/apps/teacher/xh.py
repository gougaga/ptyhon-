from flask import Blueprint
from flask_restful import Api, Resource
from flask_restful import reqparse
from flask_restful import fields, marshal_with, marshal
teacher_bp = Blueprint('teacher', __name__)
api = Api(teacher_bp)
class TeaResource(Resource):
    def get(self):
        return 'fitst teacher blueprint api'

# 参数获取：获取查询参数id http://12.0.0.1:5000/user?id=1
'''
1.导入reqparse模块
2.实例化对象/构建对象(RequestParser)
3.添加验证参数
4.启动验证
'''
class GetIDResource(Resource):
    def get(self):
         parser = reqparse.RequestParser()
         parser.add_argument('id', required=True, action='append')
         args = parser.parse_args()
         id = args['id']
         # id = args.id
         return '查询参数是{}'.format(id)
         pass

# 固定参数
'''
1.导入RequestParser类
2.实例化RequestParser对象
3.向RequsetParser对象中添加需要检验或者转换的参数声明
4.使用parse_args()方法启动检验处理
5.通过args.id或者args['id']的方法获取参数
'''
class LockResource(Resource):
    def get(self, name):
        print(name)
        return '固定参数'

# 定义用户类
class User():
    def __init__(self, name, age, pwd):
        self.name = name
        self.age = age
        self.pwd = pwd
# 序列化字段
resource_field = {
    'name': fields.String,
    'age': fields.Integer
}
# 视图类-----装饰器
class StuResource(Resource):
    @marshal_with(resource_field, envelope='data')
    def get(self):
        stu = User('zz', 15, '32131')
        return stu
        pass

# 视图类-----函数形式
class StuIndex(Resource):
    def get(self):
        u = User('asd', 20, '564654')
        return marshal(u, resource_field)
        pass
api.add_resource(TeaResource, '/tea', endpoint='tea')
api.add_resource(GetIDResource, '/user', endpoint='ge')
api.add_resource(LockResource, '/stu/<name>', endpoint='stu')
api.add_resource(StuResource, '/info', endpoint='info')
api.add_resource(StuIndex, '/teain', endpoint='teain')