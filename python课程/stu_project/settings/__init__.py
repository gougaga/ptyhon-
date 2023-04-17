class DefaultConfig(object):
    SECARY_KEY = 'wuhddimgx823^72'
class DevelopmentConfig(DefaultConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/ysys'
    # 追踪数据的修改信号
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 是否在控制台打印输出sql语句
    SQLALCHEMY_ECHO = True
