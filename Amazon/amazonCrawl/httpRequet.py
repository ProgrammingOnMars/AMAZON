import requests
import random

'''
   http 爬虫请求
'''

user_agent = [
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
]


# 封装请求函数
# def request_inter_function(url):
#     print("request url\t", url)
#     proxies = {
#         'http': 'http://lum-customer-hl_04c4aa62-zone-static:nqfk9aqs3svh@zproxy.lum-superproxy.io:22225',
#         'https': 'http://lum-customer-hl_04c4aa62-zone-static:nqfk9aqs3svh@zproxy.lum-superproxy.io:22225'
#      }
#
#     headers = {'user-agent': random.choice(user_agent)}
#     cookies = dict(cookies_are='ubid-main=130-6909477-6814051; session-id=136-3668404-3121828; session-id-time=2082787201l; unique_id=bVxZg7tNL0CHJTeHKNWBKXhJXPg4Tl6W; x-wl-uid=1rroGsm7tlEfw5b3HEEEPSVcALE0Gi5dBSFkyVPo7frABgpnD2rCPxLrBzDiorpQPHO2XuDhKNhoIBKwd/5FWIw==; sst-main=Sst1|PQHDVjy04PrJ-YC2dTupMj7kCz5ZPouyZDaaOgBzcqQIIzhgKK6F7lY37afQlJdk4O5V8VjgxcUgkN7xy4rW2kJQoIDHLudzrNyOpzXiAUdpKShoH7LsUw1LfqBA0ph_Oj3_zEKqL6Sj-2LPuV5w0sv0IszxbYC2gTEQpZV-lPIijwPcWreYfEIG9ognx8xJucc4lHUFJ2HGv8GdSOYVyBmCh0cax-U4LGP-22cRLNhKyKqN5Ng-QxILSMwmqyoH2Jc9hEAuZPThgKl8WFNMuczOXt6raBJ4f3VrHpGp6k12CnCwv8CVU3n-CXlFFuD4dZFlzDZfCjPt5gFzqJJA_qwugQ; i18n-prefs=USD; session-token="LzPO8DKZvFZcwvJNvQEWC7QBcgx3LXN2kpA102scW1wMufj5UVJRyMj1nSUlK5zo7eqmFVDXOCvyFV5qNR6WZ0f8jLN8MqP/nevxQmoRu9lcSIzdtRbRs7QUVBSDeIAXIjsWF2A7I89nS5A7NP63d8hVPA268Yf+OhOvhNYB/I3Hlm6sC+TZc/+XNzY6PoVRs/tGgextkKuqmOb7WsCJaw=="; skin=noskin; csm-hit=tb:s-X1FWMEAYGAXYXYAY7D3N|1555325090967&t:1555325102699&adb:adblk_no' )
#
#     # 除了返回状态不是200之外   还有可能连接超时, 如果连接超时了就调用自身方法重新请求
#     # response = requests.get(url, cookies=cookies, proxies=proxies, headers=headers)
#     response = requests.get(url, cookies=cookies, headers=headers)
#     # response = requests.get(url, headers=headers, proxies=proxies)
#
#     return response.text


# 封装请求函数
def request_inter_function(url):
    print("request url\t", url)
    # proxies = {
    #     'http': 'http://lum-customer-hl_04c4aa62-zone-static:nqfk9aqs3svh@zproxy.lum-superproxy.io:22225',
    #     'https': 'http://lum-customer-hl_04c4aa62-zone-static:nqfk9aqs3svh@zproxy.lum-superproxy.io:22225'
    #  }
    proxies = {
        'http': '117.63.8.163:4286',
        'https': '117.63.8.163:4286'
    }


    headers = {'user-agent': random.choice(user_agent)}
    # print("当前使用请求头\t", headers)
    # cookies = dict(cookies_are='ubid-main=130-6909477-6814051; session-id=136-3668404-3121828; session-id-time=2082787201l; unique_id=bVxZg7tNL0CHJTeHKNWBKXhJXPg4Tl6W; x-wl-uid=1rroGsm7tlEfw5b3HEEEPSVcALE0Gi5dBSFkyVPo7frABgpnD2rCPxLrBzDiorpQPHO2XuDhKNhoIBKwd/5FWIw==; sst-main=Sst1|PQHDVjy04PrJ-YC2dTupMj7kCz5ZPouyZDaaOgBzcqQIIzhgKK6F7lY37afQlJdk4O5V8VjgxcUgkN7xy4rW2kJQoIDHLudzrNyOpzXiAUdpKShoH7LsUw1LfqBA0ph_Oj3_zEKqL6Sj-2LPuV5w0sv0IszxbYC2gTEQpZV-lPIijwPcWreYfEIG9ognx8xJucc4lHUFJ2HGv8GdSOYVyBmCh0cax-U4LGP-22cRLNhKyKqN5Ng-QxILSMwmqyoH2Jc9hEAuZPThgKl8WFNMuczOXt6raBJ4f3VrHpGp6k12CnCwv8CVU3n-CXlFFuD4dZFlzDZfCjPt5gFzqJJA_qwugQ; i18n-prefs=USD; session-token="LzPO8DKZvFZcwvJNvQEWC7QBcgx3LXN2kpA102scW1wMufj5UVJRyMj1nSUlK5zo7eqmFVDXOCvyFV5qNR6WZ0f8jLN8MqP/nevxQmoRu9lcSIzdtRbRs7QUVBSDeIAXIjsWF2A7I89nS5A7NP63d8hVPA268Yf+OhOvhNYB/I3Hlm6sC+TZc/+XNzY6PoVRs/tGgextkKuqmOb7WsCJaw=="; skin=noskin; csm-hit=tb:s-X1FWMEAYGAXYXYAY7D3N|1555325090967&t:1555325102699&adb:adblk_no' )
    cookies = dict(cookies_are='session-id=135-9235188-0603150; session-id-time=2082787201l; i18n-prefs=USD; ubid-main=133-6558917-4645705; x-wl-uid=1S/euqoSzy8eZmb99Ie6FAsBKgipQjAsk5cHFm5ZuJZ6iv/ycfTdup+Ssg+VVHOoBSaCw6qhDShg=; lc-main=en_US; skin=noskin; session-token=S7CvFZ6ng0VvCPkfkzpEKiE6OChV+LF5KqpRm7mqeb+c9lrHAI1lij2lUE4FEhAhOjRWyspp/KRZQae3QWzFGuCUiOc0R0lKJ4+5GIA1aeFNBzLGuDK8utnRBlCpdEst2GmIqB0iKS0cSXLkGytv1e5N4+26pN68He9kJfE5y9v8mU2OZpjp+utKcHFZr7BB; csm-hit=tb:5DRDWRDWX92TR5F820Y9+s-2YN2R7A7C41VXYYQRCNP|1558498924717&t:1558498924717&adb:adblk_no' )

    # 除了返回状态不是200之外   还有可能连接超时, 如果连接超时了就调用自身方法重新请求
    response = requests.get(url, cookies=cookies, proxies=proxies, headers=headers)
    # response = requests.get(url, proxies=proxies, headers=headers)
    # response = requests.get(url, cookies=cookies, headers=headers)

    return response.text

# url = 'https://www.amazon.com/s?rh=n%3A283155%2Cn%3A%212334088011%2Cn%3A%212334119011%2Cn%3A6960520011&page=2'
# print(request_inter_function(url))