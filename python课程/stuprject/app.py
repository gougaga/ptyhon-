from flask import Flask
from common.model.user import db
from settings import DevelopmentConfig
from common.model.user import db
from apps.student.stu import aitwo_bp, request, jsonify
def create_flask_app(config):
    # 创建对象
    app = Flask(__name__)
    # 加载配置
    app.config.from_object(config)
    # 返回app
    return app


@aitwo_bp.route('/user/checkUser', methond=['POST'])
def get_check():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'admin' and password == '123':
        data = {'mate': {'msg': '登陆成功', 'status': 200}}
        return jsonify(data)
    else:
        data = {'mate': {'msg': '登陆失败', 'status': 500}}
        return jsonify(data)
app = create_flask_app(DevelopmentConfig)

db.init_app(app)


if __name__ == '__main__':
    app.run()
