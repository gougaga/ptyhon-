class DefaultConfig(object):
    MYSQL_HOST = '127.0.0.1'
    MYSQL_PORT = 3306
    SECRET_KEY = 'SJFDSjkhsfk#$%^&kdfjiw683942'
    pass
class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    pass