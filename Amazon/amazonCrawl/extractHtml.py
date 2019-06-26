from lxml import etree
from amazonCrawl.IOflow import *
import re
import datetime




#　详情页面提取html
def extract_details_page_html(html, details_url):
    selector = etree.HTML(html)

    res = re.findall(r'<div id="imgTagWrapperId" class="imgTagWrapper">(.*?)</div>', html, re.S)
    # 猜测更换规则
    # if len(res) > 0:
    try:
        image = re.findall(r"'colorImages': (.*?}]}),", html, re.S)[0]
        image = str(re.findall(r'"large":"(https://.*?.jpg)"', image, re.S))
    except:
        image = ''

    # 品牌
    try:
        brand = selector.xpath('//*[@id="bylineInfo"]/text()')[0].strip()
    except:
        brand = ''
    # 快递时间说明
    try:
        explanation_of_express_time = selector.xpath('//*[@id="delivery-message"]')[0].xpath('string(.)').strip()
    except:
        explanation_of_express_time = ''

    # 商品名称
    shop_name = selector.xpath('//*[@id="productTitle"]/text()')[0].strip()

    # 运费
    try:
        freight = selector.xpath('//*[@id="ourprice_shippingmessage"]/span/text()')[0].strip()
        freight = re.findall(r'\$(.*?)ship', freight, re.S)[0]
    except:
        freight = '0'
    # 　价格
    try:
        price = selector.xpath('//*[@id="priceblock_dealprice"]/text()')[0].strip()
    except:
        try:
            price = selector.xpath('//*[@id="priceblock_snsprice_Based"]/span/text()')[0].strip()
        except:
            price = selector.xpath('//*[@id="priceblock_ourprice"]/text()')[0].strip()

    # 到货时间
    try:
        arrival_time = re.findall(r'<span class="a-text-bold">(.*?)</span>', html, re.S)[0].strip()
    except:
        arrival_time = ''
    # str = "".join(tuple(arrival_time))
    # cont = re.sub(r'Get.*?,', '',arrival_time, re.S)[0].strip()
    # cont = re.findall(r'Get.*?,(.*?)', arrival_time, re.S)[0]
    # if '<span class="a-text-bold">Add-on Item</span>' in html:
    #     if 'Add-on Item' in html:
    #         return price, freight, shop_name, image, "add-on 产品，无法单独购买", brand, explanation_of_express_time

    # if 'Get' and 'FREE Shipping' in html:
    #     if 'Get' in arrival_time:
    #         return price, freight, shop_name, image, arrival_time, brand, explanation_of_express_time
    #     else:
    #         return price, freight, shop_name, image, 'Based on amazon free shipping', brand, explanation_of_express_time

    if brand == None:
        brand = ''
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
    sql = "INSERT INTO commodity_base(title, price, freight, ASIN, sku, arrival_time, picture, classification, brand, explanation_of_express_time,create_time) VALUES(\"{}\", '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(
        pymysql.escape_string(shop_name), pymysql.escape_string(price), pymysql.escape_string(freight),
        details_url.replace("https://www.amazon.com/dp/", ""),
        "U{}".format(details_url.replace("https://www.amazon.com/dp/", "")),
        pymysql.escape_string(explanation_of_express_time),
        pymysql.escape_string(image),
        "Prime Video", pymysql.escape_string(brand),
        pymysql.escape_string(explanation_of_express_time), nowTime)

    # print("sql\t", sql)
    write_sql(sql)
    print("\t\t\t\t===================================新增数据成功!==============================")
    # return price, freight, shop_name, image, "Based on amazon free shipping", brand, explanation_of_express_time


# def extract_details_page_html(html, details_url):
#     selector = etree.HTML(html)
#
#     res = re.findall(r'<div id="imgTagWrapperId" class="imgTagWrapper">(.*?)</div>', html, re.S)
#     # 猜测更换规则
#     # if len(res) > 0:
#     try:
#         image = re.findall(r"'colorImages': (.*?}]}),", html, re.S)[0]
#         image = str(re.findall(r'"large":"(https://.*?.jpg)"', image, re.S))
#     except:
#         image = ''
#
#     # 品牌
#     try:
#
#         brand = selector.xpath('//*[@id="bylineInfo"]/text()')[0].strip()
#     except:
#         brand = ''
#     # 快递时间说明
#     try:
#         explanation_of_express_time = selector.xpath('//*[@id="delivery-message"]')[0].xpath('string(.)').strip()
#     except:
#         explanation_of_express_time = ''
#
#     # 商品名称
#     shop_name = selector.xpath('//*[@id="productTitle"]/text()')[0].strip()
#
#     # 运费
#     try:
#         freight = selector.xpath('//*[@id="ourprice_shippingmessage"]/span/text()')[0].strip()
#         freight = re.findall(r'\$(.*?)ship', freight, re.S)[0]
#     except:
#         freight = '0'
#     #　价格
#     try:
#         price = selector.xpath('//*[@id="priceblock_dealprice"]/text()')[0].strip()
#     except:
#         try:
#             price = selector.xpath('//*[@id="priceblock_snsprice_Based"]/span/text()')[0].strip()
#         except:
#             price = selector.xpath('//*[@id="priceblock_ourprice"]/text()')[0].strip()
#
#
#
#     # 到货时间
#     try:
#         arrival_time = re.findall(r'<span class="a-text-bold">(.*?)</span>', html, re.S)[0].strip()
#     except:
#         arrival_time = ''
#     # str = "".join(tuple(arrival_time))
#     # cont = re.sub(r'Get.*?,', '',arrival_time, re.S)[0].strip()
#     # cont = re.findall(r'Get.*?,(.*?)', arrival_time, re.S)[0]
#     # if '<span class="a-text-bold">Add-on Item</span>' in html:
#     #     if 'Add-on Item' in html:
#     #         return price, freight, shop_name, image, "add-on 产品，无法单独购买", brand, explanation_of_express_time
#
#     # if 'Get' and 'FREE Shipping' in html:
#     #     if 'Get' in arrival_time:
#     #         return price, freight, shop_name, image, arrival_time, brand, explanation_of_express_time
#     #     else:
#     #         return price, freight, shop_name, image, 'Based on amazon free shipping', brand, explanation_of_express_time
#
#     if brand==None:
#         brand = ''
#     nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
#     sql = "INSERT INTO commodity_base(title, price, freight, ASIN, sku, arrival_time, picture, classification, brand, explanation_of_express_time,create_time) VALUES(\"{}\", '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(
#         pymysql.escape_string(shop_name), pymysql.escape_string(price), pymysql.escape_string(freight),
#         details_url.replace("https://www.amazon.com/dp/", ""),
#         "U{}".format(details_url.replace("https://www.amazon.com/dp/", "")),
#         pymysql.escape_string(explanation_of_express_time),
#         pymysql.escape_string(image),
#         "Prime Video", pymysql.escape_string(brand),
#         pymysql.escape_string(explanation_of_express_time), nowTime)
#
#     # print("sql\t", sql)
#     write_sql(sql)
#     print("\t\t\t\t===================================新增数据成功!==============================")
#     # return price, freight, shop_name, image, "Based on amazon free shipping", brand, explanation_of_express_time




# 提取搜索结果页面的Asin
def extract_asin(html):
    asin_list = re.findall(r'data-asin="(.*?)"', html, re.S)
    print(asin_list)
    print(len(asin_list))
    outer_url = []
    for shop_details_inter in asin_list:
        shop_details_inter_url = 'https://www.amazon.com/dp/{}'.format(shop_details_inter)
        outer_url.append(shop_details_inter_url)

    # print("outer_url\t",outer_url)
    return outer_url


'''
搜索结果页 商品网址
'''
def search_count(html):
    select = etree.HTML(html)
    try:
        # 网址
        seach_count = select.xpath('//*[@class="a-color-base s-line-clamp-2"]/a/@href')
        seach_count = 'https://www.amazon.com{}'.format(seach_count[0])
    except:
        'class="a-section aok-relative s-image-square-aspect"'
        seach_count = select.xpath('//*[@class="a-section aok-relative s-image-square-aspect"]/a/@href')

    return seach_count

'''
提取详情页
'''
def extract_shop_details( search_text,asin, html):
    select = etree.HTML(html)
    title = select.xpath('//*[@id="productTitle"]/text()')[0].strip()
    manufacturer = select.xpath('//*[@id="bylineInfo"]/text()')[0].strip()
    try:
        price = select.xpath('//*[@id="priceblock_ourprice"]/text()')[0].strip()
    except:
        price = 'null'

    try:
        used = select.xpath('//*[@id="olp_feature_div"]')
        finally_used = used[0].xpath("string(.)")

        seller = re.findall(r'\((.*?)\)', finally_used, re.S)[0].strip()
    except:
        seller = "null"
    print("title\t", title)
    print("finally_used\t", seller)
    print("manufacturer\t", manufacturer)
    print("price\t", price)
    print("seller\t", seller)

    findlly = "{}\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}".format(asin, title, manufacturer, price, seller)
    finally_write_txt(search_text, findlly)




# 检测当前类别下有多少页
def check_page(html):
    select = etree.HTML(html)
    result_page = select.xpath('//ul[@class="a-pagination"]//li')

    number_of_pages = result_page[len(result_page) - 2].xpath('string(.)').strip()
    # print("result_page", result_page)

    print('page num:\t',number_of_pages)
    return number_of_pages

# 左边分类页
def left_sort(html):
    select = etree.HTML(html)
    element = select.xpath('//*[@aria-labelledby="n-title"]/li')

    # 去掉最后一个列表元素, 因为那个里面装的是别的全部分类
    del(element[-1])
    # 创建列表装入分类网址
    url_list = []
    for ele in element:
        text_list = ele.xpath('.//a/@href')
        for te in text_list:
            url_list.append('https://www.amazon.com{}'.format(te.strip()))
    return url_list

# 提取商品限制条件
def extract_html(html):
    selector = etree.HTML(html)
    element = selector.xpath('//*[@class="sg-col-20-of-24 s-result-item sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28"]')
    asin = selector.xpath('//*[@class="sg-col-20-of-24 s-result-item sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28"]/@data-asin')
    title = selector.xpath('//*[@class="sg-col-20-of-24 s-result-item sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28"]//*[@class="a-size-medium a-color-base a-text-normal"]')
    price = selector.xpath(
        '//*[@class="sg-col-20-of-24 s-result-item sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28"]//*[@class="a-offscreen"]/text()')
    num = -1


    asin_list_readlly = []   # 存放满足条件的asin code
    for ele in element:
        num=num+1

        content = ele.xpath('string(.)').strip()
        if ('used' in content):
            # print(content)
            text = re.findall(r'(\(\d.*?)used.*?\)', content, re.S)[0].strip().replace("(", "")
            try:
                # 卖家必须超过5个以上
                if (int(text)>5):
                    price_str = price[num].strip()[1:] #.replace('$', '')
                    # 商品单价 ￥15 以上
                    if (float(price_str)>15):
                        # print("price\t", (float(price_str)))
                        title_text = title[num].xpath('text()')
                        # print("title\t" , title_text)
                        # print("shop number\t", text)
                        # findlly = price_str + title_text  + text
                        findlly = "{}\t\t{}\t\t\t{}\t\t\t{}".format(asin[num], title_text, price_str, text)
                        # print("findlly\t", findlly)
                        # write_txt(findlly)

                        # 装入满足条件的asin
                        asin_list_readlly.append(asin[num])

            except:
                print("exception")

    # 返回满足条件有效的asin code
    print("asin_list_readlly\t", asin_list_readlly)
    return asin_list_readlly




# 去掉 分类 java script标签
def remove_javascript(element_list):
    save_list = []  # 保存没有javaScript标志的分类网址
    for element in element_list:
        if 'javascript' not in element:
            save_list.append(element)

    # 返回清理完的list
    return save_list

# url = 'https://www.amazon.com/Naztech-High-Speed-Individually-Simultaneously-Technology/dp/B071SHZ98B/ref=sr_1_1?keywords=B071SHZ98B&qid=1555027813&s=gateway&sr=8-1'
url = 'https://www.amazon.com/s?k=B0749GV5L3&ref=nb_sb_noss'



# html = request_inter_function(url)

# search_count(html)
# print(html)
# extract_shop_details(html)