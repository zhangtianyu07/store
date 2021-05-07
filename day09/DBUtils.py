import pymysql
#写死
host = "localhost"
user = "root"
password = "root"
database = "icbc"

def update(sql,param):
    #连接数据库
    con = pymysql.connect(host=host,user=user,password=password,database=database)
    #创建控制台
    cursor = con.cursor()
    #执行SQL语句
    cursor.execute(sql,param)
    #提交
    con.commit()
    #关闭数据库
    cursor.close()
    con.close()


def select(sql,param):
    #连接数据库
    con = pymysql.connect(host=host,user=user,password=password,database=database)
    #创建控制台
    cursor = con.cursor()
    #执行SQL语句
    cursor.execute(sql,param)
    #返回数据
    return cursor.fetchall()
    #提交
    con.commit()
    #关闭数据库
    cursor.close()
    con.close()
