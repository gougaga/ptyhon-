#新建py文件，专门用来写数据库操作
import pymysql
from myspider import settings

#建立数据库连接
sqlConnect = pymysql.connect(host = settings.Mysql_host,user = settings.Mysql_user,passwd = settings.Mysql_pwd,db = settings.Mysql_db,port = settings.Mysql_port)
# 游标
cur = sqlConnect.cursor()
class Sql():
    @staticmethod
    #创建数据库表（crate）
    def create_table():
        pass
    #插入数据(insert)
    @staticmethod
    def insert_chinaz(data):
        insterStr = 'insert into chin(uname,info,ranking) values ("%s","%s","%s");'%(data['name'],data['info'],data['rank'])
        cur.execute(insterStr)
        sqlConnect.commit()
        pass

    # 更新数据(update)
    @staticmethod
    def update_chinaz(data):
        #更新数据
        pass

    # 删除数据(delete)
    @staticmethod
    def delete_chinaz(data):
        #删除数据
        pass
    #关闭数据库连接（close）
    @staticmethod
    def close_mysql():
        # cur.close() #关闭游标
        # sqlConnect.close()
        pass
    pass