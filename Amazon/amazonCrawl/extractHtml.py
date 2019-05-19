from lxml import etree
from amazonCrawl.IOflow import *
import re



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