from amazonCrawl.extractHtml import *
from amazonCrawl.httpRequet import *
from amazonCrawl.IOflow import *

'''
    起始点
'''
# search_dict = [
#     'camera',
#     'cell phone devices',
#     'personal computer'
# ]

search_dict = [
    'thin Client'
]
# search_dict = read_info()   # 遍历搜索关键词列表


for search_text in search_dict:
    index_search_url = 'https://www.amazon.com/s?k={}&ref=nb_sb_noss'.format(search_text)  # 起始搜索页

    print("start_search_url\t", index_search_url)
    html = request_inter_function(index_search_url)  # 请求网址返回网页源代码

    # print(html)
    sort_list = left_sort(html)  # 检索有多少个分类
    finally_sore_list = remove_javascript(sort_list)
    print("Current classification\t", finally_sore_list)

    # 循环遍历分类
    for sort_url in finally_sore_list:
        try:
            # 判断这个分类下有多少页
            page_num = check_page(request_inter_function(sort_url))
            # 爬取每一页
            for num in range(1, int(page_num)):
                # 调用提取函数
                html = request_inter_function('{}&page={}'.format(sort_url, num))
                try:
                    asin_list = extract_html(html)
                    for asin in asin_list:
                        # 搜索asin
                        detail_url = 'https://www.amazon.com/dp/{}'.format(asin)
                        # 去详情页爬取信息
                        extract_shop_details(search_text, asin, request_inter_function(detail_url))
                        # except:
                        #     print("Error!")
                except:
                    print("Exception")
        except:
            print("Exception1")
