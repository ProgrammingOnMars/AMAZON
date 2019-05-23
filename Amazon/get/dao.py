import pymysql
import datetime

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
    # db.close()

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
    sql = 'select * from all_url where whether_to_crawl="0" limit 0, 1 for update;'
    # sql = 'select * from all_url'
    crawl_url = cursor.execute(sql)

    for date in crawl_url:
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
        # 行加锁
        sql = "UPDATE all_url SET deal_lock_flag=1, deal_starttime='{}' WHERE id_search_address = {}; ".format(
            nowTime, item['id_search_address'])
        cursor.execute(sql)
    # conn().close()

    return cursor.fetchall()

print(read())
