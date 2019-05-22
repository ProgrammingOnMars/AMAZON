import requests
import random
from lxml import etree
import re
import pymysql


user_agent = [
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
]


#　提取html
def extract_html(html):
    selector = etree.HTML(html)

    res = re.findall(r'<div id="imgTagWrapperId" class="imgTagWrapper">(.*?)</div>', html, re.S)
    # 猜测更换规则
    if len(res) > 0:
        image = re.findall(r'(https://.*?.jpg)', res[0], re.S)[0]

        # 品牌
        brand = selector.xpath('//*[@id="bylineInfo"]/text()')[0].strip()
        # 快递时间说明
        try:
            explanation_of_express_time = selector.xpath('//*[@id="delivery-message"]')[0].xpath('string(.)').strip()
        except:
            explanation_of_express_time = None
        # 商品名称
        shop_name = selector.xpath('//*[@id="productTitle"]/text()')[0].strip()
        # 运费
        try:
            freight = selector.xpath('//*[@id="ourprice_shippingmessage"]/span/text()')[0].strip()
            freight = re.findall(r'\$(.*?)ship', freight, re.S)[0]
        except:
            freight = '0'
        #　价格
        try:
            price = selector.xpath('//*[@id="priceblock_dealprice"]/text()')[0].strip()
        except:
            try:
                price = selector.xpath('//*[@id="priceblock_snsprice_Based"]/span/text()')[0].strip()
            except:
                try:
                    price = selector.xpath('//*[@id="priceblock_ourprice"]/text()')[0].strip()
                except:
                    price = None

        if 'See All Buying Options' in html:
            price = '0'
            return price, freight, shop_name, image, '此商品暂时无法购买', brand, explanation_of_express_time

        # 到货时间
        arrival_time = re.findall(r'<span class="a-text-bold">(.*?)</span>', html, re.S)[0].strip()
        # str = "".join(tuple(arrival_time))
        # cont = re.sub(r'Get.*?,', '',arrival_time, re.S)[0].strip()
        # cont = re.findall(r'Get.*?,(.*?)', arrival_time, re.S)[0]
        if '<span class="a-text-bold">Add-on Item</span>' in html:
            if 'Add-on Item' in html:
                return price, freight, shop_name, image, "add-on 产品，无法单独购买", brand, explanation_of_express_time

        if 'Get' and 'FREE Shipping' in html:
            if 'Get' in arrival_time:
                return price, freight, shop_name, image, arrival_time, brand, explanation_of_express_time
            else:
                return price, freight, shop_name, image, 'Based on amazon free shipping', brand, explanation_of_express_time


        return price, freight, shop_name, image, "Based on amazon free shipping", brand, explanation_of_express_time

    else:
        # 图片规则 (图书类型商品)
        try:
            img_content = re.findall(r'<div id="img-canvas".*?>(.*?)</div>', html, re.S)[0]
            pic_img_url = re.findall(r'(https://.*?.jpg)', img_content, re.S)[0]
        except:
            # pic_img_url = re.findall(r'(https://.*?.jpg)', html, re.S)[1]
            pic_img_url = ''
        # 运费
        try:
            # pic_freight = re.findall(r'+(.*?)shipping', html, re.S)
            pic_freight = selector.xpath('//*[@class="a-section a-spacing-mini"]/*[@class="a-row"]/text()')[0]
            pic_freight = re.findall(r'\+(.*?)s', pic_freight, re.S)[0]
        except:
            try:
                pic_freight = selector.xpath('//*[@class="a-size-small a-color-secondary shipping3P"]/text()')[0]
                pic_freight = re.findall(r'\+(.*?)s', pic_freight, re.S)[0]
            except:
                pic_freight = '图书免运费'
        # 商品名称
        pic_shop_name = selector.xpath('//*[@id="productTitle"]/text()')[0].strip()
        # 到货时间
        arrival_time = "Based on amazon free shipping"

        # 　价格
        try:
            pic_price = re.findall(r'<span class="a-size-medium a-color-price offer-price a-text-normal">(.*?)</span>', html, re.S)[0]
        except:
            if 'See All Buying Options' in html:
                try:
                    pic_price = re.findall(r'<span class="a-size-medium a-color-price offer-price a-text-normal">(.*?)</span>', html, re.S)[0]
                    return pic_price, pic_freight, pic_shop_name, pic_img_url, '此商品暂时无法购买'
                except:
                    return "0", pic_freight, pic_shop_name, pic_img_url, '此商品暂时无法购买'
        return pic_price, pic_freight, pic_shop_name, pic_img_url, arrival_time

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

# 封装请求函数
def request_inter_function(url):
    print("request url\t", url)
    proxies = {
        'http': 'http://lum-customer-hl_04c4aa62-zone-static:nqfk9aqs3svh@zproxy.lum-superproxy.io:22225',
        'https': 'http://lum-customer-hl_04c4aa62-zone-static:nqfk9aqs3svh@zproxy.lum-superproxy.io:22225'
     }

    headers = {'user-agent': random.choice(user_agent)}
    cookies = dict(cookies_are='ubid-main=130-6909477-6814051; session-id=136-3668404-3121828; session-id-time=2082787201l; unique_id=bVxZg7tNL0CHJTeHKNWBKXhJXPg4Tl6W; x-wl-uid=1rroGsm7tlEfw5b3HEEEPSVcALE0Gi5dBSFkyVPo7frABgpnD2rCPxLrBzDiorpQPHO2XuDhKNhoIBKwd/5FWIw==; sst-main=Sst1|PQHDVjy04PrJ-YC2dTupMj7kCz5ZPouyZDaaOgBzcqQIIzhgKK6F7lY37afQlJdk4O5V8VjgxcUgkN7xy4rW2kJQoIDHLudzrNyOpzXiAUdpKShoH7LsUw1LfqBA0ph_Oj3_zEKqL6Sj-2LPuV5w0sv0IszxbYC2gTEQpZV-lPIijwPcWreYfEIG9ognx8xJucc4lHUFJ2HGv8GdSOYVyBmCh0cax-U4LGP-22cRLNhKyKqN5Ng-QxILSMwmqyoH2Jc9hEAuZPThgKl8WFNMuczOXt6raBJ4f3VrHpGp6k12CnCwv8CVU3n-CXlFFuD4dZFlzDZfCjPt5gFzqJJA_qwugQ; i18n-prefs=USD; session-token="LzPO8DKZvFZcwvJNvQEWC7QBcgx3LXN2kpA102scW1wMufj5UVJRyMj1nSUlK5zo7eqmFVDXOCvyFV5qNR6WZ0f8jLN8MqP/nevxQmoRu9lcSIzdtRbRs7QUVBSDeIAXIjsWF2A7I89nS5A7NP63d8hVPA268Yf+OhOvhNYB/I3Hlm6sC+TZc/+XNzY6PoVRs/tGgextkKuqmOb7WsCJaw=="; skin=noskin; csm-hit=tb:s-X1FWMEAYGAXYXYAY7D3N|1555325090967&t:1555325102699&adb:adblk_no' )

    # 除了返回状态不是200之外   还有可能连接超时, 如果连接超时了就调用自身方法重新请求
    # response = requests.get(url, cookies=cookies, proxies=proxies, headers=headers)
    response = requests.get(url, cookies=cookies, headers=headers)

    return response.text

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


# 提取页面的Asin
def extract_asin(html):
    asin_list = re.findall(r'data-asin="(.*?)"', html, re.S)
    print(asin_list)
    print(len(asin_list))
    outer_url = []
    for shop_details_inter in asin_list:
        shop_details_inter_url = 'https://www.amazon.com/dp/{}'.format(shop_details_inter)
        outer_url.append(shop_details_inter_url)

    print(outer_url)
    return outer_url

url = "https://www.amazon.com/dp/B078M7Q682?ref_=Oct_LDealsC_328182011_1&pf_rd_p=1fa367c8-ef57-5466-b15a-86c24bad898c&pf_rd_s=merchandised-search-8&pf_rd_t=101&pf_rd_i=328182011&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=3X29P6P2N302PDD5SBR3&pf_rd_r=3X29P6P2N302PDD5SBR3&pf_rd_p=1fa367c8-ef57-5466-b15a-86c24bad898c"


# 读取待爬取url
def read():
    db = pymysql.connect("120.79.192.201", "root", "1qaz2wsx#EDC", "amazon")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # 使用cursor()方法获取操作游标
    # sql = 'select id, url from all_url where whether_to_crawl="0" limit 0, 100 '
    sql = 'select * from all_url'
    cursor.execute(sql)

    # conn().close()

    return cursor.fetchall()



num = 0
for item in read():
    num += 1
    print("当前请求次数\t", num)
    print("url\t",item['url'])
    d_html = request_inter_function(item['url'])
    asin_list = extract_asin(d_html)
    for detalis_url in asin_list:

        # 返回数据集合
        try:
            # 返回商品详情页网页源代码
            html = request_inter_function(detalis_url)
            ret_data_list = list(extract_html(html))

            print("ret_data_list\t", ret_data_list)

            sql = "INSERT INTO commodity_base(title, price, freight, ASIN, sku, arrival_time, picture, classification, brand, explanation_of_express_time) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(ret_data_list[2], ret_data_list[0], ret_data_list[1], url.replace("https://www.amazon.com/dp/", ""), "U{}".format(url.replace("https://www.amazon.com/dp/", "")),ret_data_list[4], ret_data_list[3], "Toys & Games", ret_data_list[5], ret_data_list[6])
            write_sql(sql)

            print("新增数据成功!")
        except:
            print("error!")