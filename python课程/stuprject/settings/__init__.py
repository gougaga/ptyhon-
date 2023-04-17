class DefaultConfig(object):
    SECERY_KET = 'asdlajh546&654^'

class DevelopmentConfig(DefaultConfig):
    SQLALCHEMY_DATABASE_URI ='mysql+pymysql://root:123456@127.0.0.1:3306/jkk'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True