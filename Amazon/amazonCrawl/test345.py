from amazonCrawl.httpRequet import *
import re
from lxml import etree
import re
from amazonCrawl.IOflow import *

class price:

    # 读取asin
    def read_text_asin(self, path):
        # 第二种方法
        data = []
        for line in open(path, "r"):  # 设置文件对象并读取每一行文件
            data.append(line)  # 将每一行文件加入到list中

        list = []
        for i in data:
            list.append(i.strip())
        return list

    # 写入txt文件
    def write_txt(self, content):
        f = open(r'去重cell phone devices.txt', 'a', encoding='utf8')
        f.write(content)
        f.write("\n")
        f.close()


    # 爬取详情信息
    def details(self, html):
        select = etree.HTML(html)

        details = select.xpath('//*[@id="olpOfferListColumn"]//*[@class="a-row a-spacing-mini olpOffer"]')

        # 价格数组
        price_list = []

        # 遍历循环
        for deta in details:

            text = deta.xpath("string(.)")

            if "Like New" not in text:

                if "Refurbished" not in text:
                    if "Good" not in text:
                        if "Like New" not in text:
                            if "Acceptable" not in text:

                                try:
                                    price = deta.xpath('.//*[@class="a-size-large a-color-price olpOfferPrice a-text-bold"]/text()')[0].strip().replace("$", "")
                                    price_list.append(float(price))
                                except:
                                    price = 0
                                    price_list.append(float(10))

        if(len(price_list)>0):
            print("price_list\t", price_list)
            print("price_list\t", min(price_list))
            return min(price_list)   # 返回最小价格数
        else:
            print("elese")
            return 0


if __name__ == "__main__":
    run_main = price()

    file_path = r"c:\Users\XY\Desktop\去重cell phone devices.txt"

    list = run_main.read_text_asin(file_path)


    for asin in list:

        url = 'https://www.amazon.com/gp/offer-listing/{}'.format(asin)
        try:
            html = request_inter_function(url)

            min_price = run_main.details(html) # 返回最小价格数

            run_main.write_txt("{}\t\t{}\t\t\t{}".format(asin, min_price, url))   # 写入
        except:
            print("exception")


