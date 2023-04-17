from flask import Flask
# 导入配置
from settings import DefaultConfig
from flask import request

requestss = Flask(__name__)

@requestss.route('/stu/')
def user_info():

    user_id_1 = request.args['userid']

    user_id_2 = request.args.get('userid')
    return 'user_id_1: {}, user_id_2: {}'.format(user_id_1, user_id_2)

if __name__ == '__main__':
    requestss.run()