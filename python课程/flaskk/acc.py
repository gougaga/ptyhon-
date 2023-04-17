from flask import Flask
from flask import request, redirect, render_template
# 导入配置
app = Flask(__name__)

@app.route('/login',methods=['POST', 'GET'])
def login():
    # 获取form表单中的用户名
    username = request.form.get('uname')# FORM表单
    # 获取form表单中的密码
    password = request.form.get('pwd')# FORM表单
    # 用户名与密码的判断
    if username == 'admin' and password == 'admin123':
        return render_template('login.html')
    else:
        return redirect('http://www.baidu.com')

@app.route('/loginn')
def loginn():
    # 获取form表单中的用户名
    username = request.args.get('uname')# FORM表单
    # 获取form表单中的密码
    password = request.args('pwd')# FORM表单
    # 用户名与密码的判断
    if username == 'admin' and password == 'admin123':
        return render_template('login.html')
    else:
        return redirect('http://www.baidu.com')


@app.route('/upload', methods=['POST'])
def upload_file():
    # 获取前端传递过来的文件对象
    img = request.files.get('pic')
    # 获取文件对象的文件名
    file_name = img.filename
    # 保存文件对象
    img.save(file_name)
    return '上传成功'

@app.route('/')
def index():
    # 打印请求头信息
    print(request.headers)
    print('-'*50)
    # 打印请求方法
    print(request.method)
    print('-'*50)
    # 打印请求的url
    print(request.url)
    return 'other args'
if __name__ == '__main__':
    app.run( port=1234)