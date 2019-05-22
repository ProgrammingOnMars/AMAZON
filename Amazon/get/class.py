from amazonCrawl.httpRequet import *
from get.dao import *
from lxml import etree
import re

'''
    查看每个二级分类下有多少页  一般都是超过400页
'''

# 查看页数
def page_num(html):
    select = etree.HTML(html)
    page_num_ber = select.xpath('//*[@id="pagn"]/span[6]/text()')[0].strip()
    # print(html)
    print("page_num_ber\t",page_num_ber)

    return page_num_ber

def extract(html):
    select = etree.HTML(html)
    element = select.xpath('//*[@class="a-unordered-list a-nostyle a-vertical s-ref-indent-one"]//li/span/a/@href')

    print(element)
    print(len(element))
    quit()
    for ele in element:
        url = "https://www.amazon.com{}".format(ele)
        print("url\t",url)

        p_num = page_num(request_inter_function(url))

        rh = "https://www.amazon.com/s?{}".format(re.findall(r'(rh=.*?&)', ele, re.S)[0])

        quit()
        for n in range(1, int(p_num)):
            url = "{}page={}".format(rh, n)

            print("url\t", url)

            sql = 'insert into all_url (url) values("{}")'.format(url)
            write_sql(sql)


        sql = 'insert into next_url (url, page_num) values("{}", "{}")'.format(url, p_num)
        write_sql(sql)



    # print(len(element))


#
# url = 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Dtoys-and-games&field-keywords='
# html = request_inter_function(url)
#
# extract(html)

url = 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Dtoys-and-games&field-keywords='
html = request_inter_function(url)

page_num(html)