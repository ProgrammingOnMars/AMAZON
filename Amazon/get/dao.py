import pymysql

def write_sql(sql):
    # 打开数据库连接
    db = pymysql.connect("120.79.192.201", "root", "1qaz2wsx#EDC", "amazon")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 插入语句
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()

    # 关闭数据库连接
    db.close()

#　连接数据库
def conn():
    db = pymysql.connect("120.79.192.201", "root", "1qaz2wsx#EDC", "amazon")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    return cursor


# 读取未爬取url
def read():
    db = pymysql.connect("120.79.192.201", "root", "1qaz2wsx#EDC", "amazon")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 使用cursor()方法获取操作游标
    sql = 'select * from all_url where whether_to_crawl="0" limit 0, 10'
    # sql = 'select * from all_url'
    cursor.execute(sql)

    # conn().close()

    return cursor.fetchall()

print(read())
