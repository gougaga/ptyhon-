from flask import Flask, g
main = Flask(__name__)

@main.route('/')
def hello_word():
    return 'Hello World'

@main.route('/home')
def home():
    return '这是主页'

def get_info():
    name = g.u_name
    id = g.u_id
    print('名字{}学号{}'.format(name, id))

@main.route('/getg')
def get_g():
    g.u_name = 'ss'
    g.u_id = 123
    get_info()
    return 'g变量得使用'
if __name__ == '__main__':
    main.run()