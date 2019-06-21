import requests
import random
from lxml import etree
import re
import pymysql
import datetime
from amazonCrawl.httpRequet import *
from amazonCrawl.IOflow import *
from amazonCrawl.extractHtml import *
import threading
import time



# 读取待爬取url
def read():
    db = pymysql.connect("120.79.192.201", "root", "1qaz2wsx#EDC", "amazon")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 使用cursor()方法获取操作游标
    # sql = 'select id, url from all_url where whether_to_crawl="0" limit 0, 100 '
    sql = 'select * from all_url where climb="0" limit 0, 10 for update'
    cursor.execute(sql)
    crawl_url = cursor.fetchall()
    for date in crawl_url:
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
        # 行加锁
        sql = "UPDATE all_url SET climb=1, date='{}' WHERE id = {}; ".format(
            nowTime, date['id'])
        cursor.execute(sql)
    # conn().close()
    # conn().close()
    db.commit()

    return crawl_url


def main():

    num = 0
    for item in read():
        num += 1
        try:
            d_html = request_inter_function(item['url'])

            # browser.get(item['url'])
            # browser.implicitly_wait(20)
            # print(d_html)
            # asin_list = extract_asin(browser.page_source)
            asin_list = extract_asin(d_html)
            print("asin_list\t", asin_list)
            for detalis_url in asin_list:
                print("当前请求次数\t", num)
                # 返回商品详情页网页源代码
                html = request_inter_function(detalis_url)

                extract_details_page_html(html, detalis_url)
        except:
            print("报错@继续执行下去")




threads = []
threads.append(threading.Thread(target=main))
threads.append(threading.Thread(target=main))
threads.append(threading.Thread(target=main))
threads.append(threading.Thread(target=main))
threads.append(threading.Thread(target=main))
threads.append(threading.Thread(target=main))
threads.append(threading.Thread(target=main))
threads.append(threading.Thread(target=main))
threads.append(threading.Thread(target=main))
threads.append(threading.Thread(target=main))


if __name__ == '__main__':
    for t in threads:
        t.start()


# url = "https://www.amazon.com/dp/B07JBNS2TS"
# html = request_inter_function(url)
# print(html)
# print(extract_asin(html))