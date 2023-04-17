from flask import Blueprint
from flask_restful import Api, Resource
from flask_restful import fields, marshal
from flask import Flask
from flask import request, redirect, render_template, jsonify
from flask_restful import reqparse
from common.model.user import db, UserModel

aitwo_bp = Blueprint('aitwo', __name__)
api = Api(aitwo_bp)
# 序列化字段
aiResource = {
    'u_id': fields.Integer,
    'user_id': fields.String,
    'u_name': fields.String,
    'u_pwd': fields.String,
    'user_fullname': fields.String
}

@aitwo_bp.route('/user/checkuser', methond=['POST'])
def get_check():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'admin' and password == '123':
        data = {'mate': {'msg': '登陆成功', 'status': 200}}
        return jsonify(data)
    else:
        data = {'mate': {'msg': '登陆失败', 'status': 500}}
        return jsonify(data)