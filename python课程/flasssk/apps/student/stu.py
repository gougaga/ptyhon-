'''
进行数据库的数据添加和查询

'''
from flask import Blueprint
from flask_restful import Api, Resource
from flask_restful import fields, marshal
from flask_restful import reqparse
from common.model.user import db, UserModel

# 实例化对象
aitwo_bp = Blueprint('aitwo', __name__)
api = Api(aitwo_bp)
# 序列化字段
aiResource = {
    'id': fields.Integer,
    'u_name': fields.String,
    'u_pwd': fields.String
}

# 类视图
class aitwoResource(Resource):
    def __init__(self):
        self.reqps = reqparse.RequestParser()
    def get(self):
        # 查询所有数据
        #res = UserModel.query.all()
        # 查询第一条数据
        #res = UserModel.query.first()
        # 查询数据表里的第二条数据
        #res = UserModel.query.get(2)
        # 查询指定参数的数据
        res = UserModel.query.filter_by(u_name='asd').first()
        return marshal(res, aiResource)

    def post(self):
        '''添加学生'''
        # 添加参数
        self.reqps.add_argument('id', type=int)
        self.reqps.add_argument('u_name', type=str)
        self.reqps.add_argument('u_pwd', type=str)
        # 校验
        args = self.reqps.parse_args()
        # 获取
        id = args['id']
        u_name = args['u_name']
        u_pwd = args['u_pwd']
        sub = UserModel(id=id, u_name=u_name, u_pwd=u_pwd)
        try:
            db.session.add(sub)
            db.session.commit()
        except Exception as e:
            print(e)
            return '学生添加失败'
        return '{}-学生添加成功'.format(u_name)

    def put(self):
        # 修改或者更新数据（根据id）
        self.reqps.add_argument('id')
        self.reqps.add_argument('u_name')
        self.reqps.add_argument('u_pwd')
        args = self.reqps.parse_args()
        id = args['id']
        u = UserModel.query.filter_by(id=id)
        if u:
            u.update(args)    # 请求传入字段和数据库字段完全一样时，可使用update
            # 不一致
            # u.u_name=args['u_name']
            # u.u_pwd = args['u_pwd']
            db.session.commit()
            return '修改成功'
        else:
            return '查无此人/修改失败'

    def delete(self):
        # 删除数据（根据name删除）
        self.reqps.add_argument('name')
        args = self.reqps.parse_args()
        name = args['name']
        try:
            UserModel.query.filter_by(u_name=name).delete()
            db.session.commit()
            return '删除成功'
        except Exception as e:
            print('删除实拍', e)
            return '删除失败'
# 给路由
api.add_resource(aitwoResource, '/add', endpoint='add')