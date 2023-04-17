from flask import Blueprint, request, jsonify, json
from common.model.user import db, StuModel

stu_db = Blueprint('stu', __name__)
@stu_db.route('/user/checkUser',methods=['POST'])
def stu_info():
    #username = request.form.get('username')
    #password = request.form.get('password')
    json_data = json.loads(request.get_data().decode('utf-8'))
    username = json_data.get('username')
    password = json_data.get('password')
    if username == 'admin' and password == '123':
        data = {"mate": {"msg": "登录成功", "status": 200}}
        return jsonify(data)
    else:
        data = {"mate": {"msg": "内部错误", "status": 500}}

        return jsonify(data)


@stu_db.route('/user/add', methods=['POST'])
def get_add():
    json_data = json.loads(request.get_data().decode('utf-8'))
    user_pw = json_data.get('user_pw')
    user_name = json_data.get('user_name')
    user_fullname = json_data.get('user_fullname')
    u = StuModel(user_pw=user_pw, user_name=user_name, user_fullname=user_fullname)
    if u:
        db.session.add(u)
        db.session.commit()
        data = {'mate': {'msg': '添加成功', 'status': 200}}
        return jsonify(data)
    else:
        data = {'mate': {'msg': '添加失败', 'status': 500}}
        return jsonify(data)


@stu_db.route('/user/list', methods=['GET'])
def get_li():
    # 查询所有信息
    res = StuModel.query.all()
    li = []
    for u in res:
        data = {'user_id': u.user_id, 'user_pw': u.user_pw, 'user_name': u.user_name, 'user_fullname': u.user_fullname}
        li.append(data)
    return jsonify({'data': li})



@stu_db.route('/user/update', methods= ['POST'])
def get_update():
    pass
