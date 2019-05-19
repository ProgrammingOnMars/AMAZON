import tweepy
from amazonCrawl.httpRequet import *
import re
import pymysql
import json

def conn_object():


   connect = pymysql.Connect(
      host='120.79.192.201',
      port=3306,
      user='root',
      passwd='1qaz2wsx#EDC',
      db='corresponding_information',
      charset='utf8',
      cursorclass=pymysql.cursors.DictCursor
   )
   return connect


# 写入txt文件
def finally_write_txt(content):
    f = open(r'all.txt', 'a', encoding='utf8')
    f.write(content)
    f.write("\n")
    f.close()

def extract(html):

   # 所有10个
   in_le = re.findall(r'<div class="a-row a-spacing-mini olpOffer".*?>.*?</form>', html, re.S)

   # print(in_le)
   # print("content\t", len(in_le))

   # 存放所有符合条件的price列表
   calculation_price = []

   for con in in_le:

      # 必须是prime商品
      if '<span class="supersaver">' in con:
         element = re.findall(r'<span class="a-size-medium olpCondition a-text-bold">(.*?)</span>', con, re.S)
         for ele in element:
            # 必须是全新商品
            if(ele.strip() == "New"):

               price = re.findall(r'<span class="a-size-large a-color-price olpOfferPrice a-text-bold">(.*?)</span>', con, re.S)[0].strip().replace("$", "").replace(",", "")
               calculation_price.append(float(price))   # 将价格添加进去



   print("打印所有price价格列表\t", calculation_price)

   calculation_price.sort()



   try:
      print("打印最小price的价格列表\t", calculation_price[0])
      return calculation_price[0]
   except:
      return 0



# url = 'https://www.amazon.com/gp/offer-listing/B07CY79CKZ/ref=sr_1_3_olp?keywords=All-In-One+Desktop&qid=1556630554&s=gateway&sr=8-3'




connect = conn_object()

cursor = connect.cursor()
cursor.execute("select * from corresponding")


for asin in cursor.fetchall():
   json_str = json.dumps(asin)
   jso_cit = eval(json_str)

   print("sql fetool num\t", str(jso_cit['ASIN']))
   #　商家列表页面
   detail_url = 'https://www.amazon.com/gp/offer-listing/{}'.format(jso_cit['SKU'])

   try:
      minimum_price = extract(request_inter_function(detail_url))
   except:
      minimum_price = "Add to cart to see product details."
   conten = '{}\t\t{}\t\t{}'.format(str(jso_cit['ASIN']) ,str(jso_cit['SKU']), str(minimum_price))
   finally_write_txt(conten)


