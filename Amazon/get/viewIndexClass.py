'''
  查看亚马逊首页有哪些分类
'''
from amazonCrawl.httpRequet import *
'''
  首页url
'''

index_url = "https://www.amazon.com/gp/homepage.html/ref=wt_urltypo/"


html = request_inter_function(index_url)



print(html)



