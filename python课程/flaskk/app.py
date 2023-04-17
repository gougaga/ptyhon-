# 实现Flask入门应用
# 实现步骤：
# 1.导入Flask类
from flask import Flask, jsonify, make_response
from flask import request, url_for, render_template, redirect
# 导入配置
from settings import DefaultConfig, DevelopmentConfig

# 2.实例化Flask对象
app = Flask(__name__)

# 从配置对象中加载配置
app.config.from_object(DefaultConfig)
# 3.编写路由与视图

@app.route('/', methods=['GET', 'POST'], endpoint='sys')
def hi_windows():
    return render_template('index.html')


@app.route('/home')
def aome():
    # 重新向外连接
    #return redirect('https://www.baidu.com')

    # 重定向内部连接 方式一
    #return redirect('/')
    # 重定向内部连接 方式二

    return redirect(url_for('sys'))
    # return '这是主页'



@app.route('/dy')
def index():
    # get方式调用配置
    mysql_port = app.config.get('MYSQL_PORT')
    print(mysql_port)
    # 字典键值方式调用配置
    mysql_host = app.config['MYSQL_HOST']
    print(mysql_host)
    return 'load co from object'


@app.route('/eham')
def home():
    return 'asd页'


@app.route('/two')
def two():
    a_name = app.config.from_envvar('settings')
    print(a_name)
    b_name = app.config['USERNAME']
    print(b_name)
    return '环境变量加载'


@app.route('/sy', methods=['GET', 'POST'], endpoint='sy')
def hello_world():
    return 'Hello 大笨猪'

# print(app.url_map)


@app.route('/article/<int:article_id>')
def get_id(article_id):
    print(article_id)
    return '这是{}篇文章页面'.format(article_id)


# 自定义转换器实例
# 导入BaseConverter
from werkzeug.routing import BaseConverter
# 自定义Converter类
class phoneConverter(BaseConverter):
    regex = r'1[1-9]\d{9}'
# 添加converter容器
app.url_map.converters['phone'] = phoneConverter
# 使用自定义转换器

@app.route('/user/<phone:user_id>')
def user_info(user_id):
    return user_id


'''输入数字返回数字'''
@app.route('/number/<int:number_id>')
def nu_id(number_id):
    print(number_id)
    return '返回的数字是：{},蔡萌是个大笨猪'.format(number_id)



@app.route('/stu/')
def stu_id():
    s_id = request.args.get('id')
    s_name = request.args['name']
    return '当前{}ID为{}'.format(s_name, s_id)


@app.route('/goods/page=<page_id>')
def ye_id(page_id):
    ps = request.args.get('pagesize')
    return '当前为第{}页, 页面包含{}条数据'.format(page_id, ps)


@app.route('/studenets/names=<name_name>')
def stu_student(name_name):
    n = request.args.get('age')
    return '当前为{},年龄{}岁'.format(name_name, n)

'''响应json数据与元组'''
# json数据
@app.route('/json')
def get_json():
    data = {
        "name": "ff",
        "class": "2"
    }
    return jsonify(data)

# 元组形式
# 可以返回一个元组，这样的元组必须是（response，status，headers）的形式，且至少包含2个元素。status值会覆盖状态代码，headers可以是一个字典或列表，作为额外的消息头
@app.route('/index', endpoint='idx')
def index():
    #return ('要返回的字符出串', '6699状态码', {'author': 'jeremy'}字典是设置在响应头中的键值对信息)
    #return ('要返回的字符串', 6699, {'author': 'jeremy'})
    # 响应字符串
    resp = make_response('自定义的响应字符串')
    # 响应头键值对
    resp.headers['author'] = 'jeremy'
    # 状态码与状态码提示信息
    resp.status = '404'
    # 注意：响应头键值对与状态码提示信息均为英文，否则抛异常
    return resp

# 4.启动服务器
if __name__ == '__main__':
    app.run( port=1234)