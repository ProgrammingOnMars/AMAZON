import pymysql
import re
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

db = pymysql.connect("120.79.192.201", "root", "1qaz2wsx#EDC", "amazon")

cursor = db.cursor(pymysql.cursors.DictCursor)

# cursor.execute("update all_url set climb=0")
cursor.execute("select * from commodity_base")
info_list = cursor.fetchall()
print(type(info_list))
for item in info_list:
    print(item['picture'])


    image = re.findall(r'"large":"(https://.*?.jpg)"', item['picture'], re.S)
    print("ima\t",type(image))
    if image:
        sql = "update commodity_base set picture='{}' where id='{}'".format(pymysql.escape_string((str(image))), item['id'])
        print(sql)
        cursor.execute(sql)
        print("列表不为空")
    else:
        print("列表为空")

db.commit()


