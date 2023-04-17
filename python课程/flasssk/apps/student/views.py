'''
0.导入蓝图
1.创建蓝图 / 实例化对象
2.添加蓝图路由
3.注册蓝图（在启动文件中书写（app.py)中）
'''

# 导入蓝图
from flask import Blueprint

# 创建蓝图/实例化蓝图对象
address_bp = Blueprint('apps', __name__)

# 添加蓝图路由
@address_bp.route('/index')
def index():
    return 'Blueprint'