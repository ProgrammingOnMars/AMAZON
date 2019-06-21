
from amazonCrawl.IOflow import *
from amazonCrawl.httpRequet import *

from amazonCrawl.extractHtml import *

# 打开数据库连接
db = pymysql.connect("120.79.192.201", "root", "1qaz2wsx#EDC", "amazon")
cursor = db.cursor()
sql = ''
num = 0
for page_num in range(1, 400):
    num=num+1
    print("write\t", num)
    url = 'https://www.amazon.com/s?rh=n%3A165796011%2Cn%3A%21165797011%2Cn%3A166777011&page={}'.format(page_num)
    # html = request_inter_function(str_tr)


    # 使用cursor()方法获取操作游标
    sql = 'insert into all_url (url, classification, climb) values("{}", "Feeding", "0")'.format(url)
    # SQL 插入语句
    # 执行sql语句
    cursor.execute(sql)

# 提交到数据库执行
db.commit()
# 关闭数据库连接
cursor.close()
