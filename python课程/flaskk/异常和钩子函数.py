from flask import Flask, jsonify, make_response, sessions
from flask import request, url_for, render_template, redirect, session, abort
# 导入配置
from settings import DefaultConfig
app = Flask(__name__)
'''异常'''
@app.route('/abo')
def get_abo():
    try:
        ret = 100/0
    except:
        abort(500)
    return '异常信息'
@app.errorhandler(500)
def get_info(e):
    return '服务器崩溃'


'''钩子函数'''
'''
请求钩子
（1）.请求钩子介绍：flask的请求钩子类似于Django的中间件, flask的请求钩子分为四种,如下所示：
before_first_request： 请求处理前执行，只执行一次before_request:请求处理前执行,每次请求处理前都会执行after_request:请求处理后执行,但其是在请求无异常的基础上执行的,该钩子接受一个参数为响应对象,并且钩子函数最后需要将参数传递来的响应return返回
teardown_request：请求处理后执行，其无论请求是否存在异常都会执行,该钩子也接受一个参数为异常信息
'''
@app.route('/gz')
def get_gz():
    print('函数执行了')
    return 'index page'

# 第一次请求处理前执行，后续请求到来不执行，只执行一次
@app.before_first_request
def brf():
    print('before_first_request')

# 每个请求到来前都执行一次
@app.before_request
def bre():
    print('before_request')

# 请求处理后无异常执行该钩子，有异常也有可能执行
@app.after_request
def are(e):
    print('after_request')
    return e

'''
请求处理后，无论存在异常是否，都会执行该请求钩子
注意：该钩子必须接受一个异常信息形参
条模式下不生效
'''
@app.teardown_request
def tea(e):
    print('teardown_request')
    return e

if __name__ == '__main__':
    app.run(port=1234)

