from flask import Flask, jsonify, make_response, sessions
from flask import request, url_for, render_template, redirect, session
# 导入配置
from settings import DefaultConfig
app = Flask(__name__)
app.config['SECRET_KEY'] = ')%&^$^$#^&^%^&'

# cook设置
@app.route('/set')
def set_coo():
    resp = make_response('设置cookie')
    resp.set_cookie('ck', 'rgzn')
    return resp
    pass

# cookie获取
@app.route('/get')
def get_coo():
    info = request.cookies.get('ck')
    return info

# session设置
@app.route('/sets')
def get_sesion():
    session['ck'] = 'rengongzhineng'
    return 'session设置成功'

# session获取
@app.route('gets')
def get_session():
    see = session.get('ck')
    return see

# session删除
@app.route('/dels')
def del_session():
    resp = make_response('删除session')
    resp.delete_cookie('session')
    return resp
if __name__ == '__main__':
    app.run( port=4567)