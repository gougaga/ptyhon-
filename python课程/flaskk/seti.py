from flask import Flask

apple = Flask(__name__)

apple.config.from_pyfile('setting.py')
@apple.route('/')
def index():

    mysql_port = apple.config.get('MYSQL_PORT')
    print(mysql_port)
    mysql_host = apple.config['MYSQL_HOST']
    print(mysql_host)
    return 'HELLO 蔡萌'
if __name__ == '__main__':
    apple.run()