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

def query(url):
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "12345", "excel")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 插入语句
    sql = """select * from data where url='{}'""".format(url)
    print(sql)
    # 执行sql语句
    cursor.execute(sql)

    count = cursor.fetchall()

    print(count)
    print(len(count))
    # 提交到数据库执行
    db.commit()
    # 关闭数据库连接
    db.close()

    if len(count) > 0:
        return True
    else:
        return False
'''
写入文件内容
'''

# 读取搜索关键词txt
def read_info():
    content = []
    f = open(r'关键词.txt')
    line = f.readline()
    while line:
        # print(line, end='')
        line = f.readline()
        content.append(line)
    f.close()
    return content



# 写入txt文件
def finally_write_txt(path, content):
    f = open(r'符合条件的{}.txt'.format(path), 'a', encoding='utf8')
    f.write(content)
    f.write("\n")
    f.close()

# 写入txt文件
def new_finally_write_txt(path ,content):
    f = open(r'符合条件的camera.txt', 'a', encoding='utf8')
    f.write(content)
    f.write("\n")
    f.close()

# 写入txt文件
def write_txt(content):
    f = open(r'符合条件的personal computer.txt', 'a', encoding='utf8')
    f.write(content)
    f.write("\n")
    f.close()


# 日志
def log(content):
    f = open(r'personal computer-Journal.txt', 'a', encoding='utf8')
    f.write(content)
    f.write("\n")
    f.close()