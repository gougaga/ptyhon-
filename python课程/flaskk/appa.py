# app封装
# 实现过程
# 1.导入Flask类
from flask import Flask
# 配置类封装在settings文件中
from settings import DefaultConfig, DevelopmentConfig

# 封装app的工厂函数
def create_flask_appa(config):
    appa = Flask(__name__)
    # 从对象加载配置
    appa.config.from_object(config)
    return appa

appa = create_flask_appa(DevelopmentConfig)
@appa.route('/')
def index():
    return 'flask Hello'

if __name__ == '__main__':
    appa.run()