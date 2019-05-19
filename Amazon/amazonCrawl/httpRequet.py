import requests
import random

'''
   http 爬虫请求
'''

user_agent = [
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
]


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
    response = requests.get(url, cookies=cookies, proxies=proxies, headers=headers)
    # response = requests.get(url, cookies=cookies, headers=headers)
    # response = requests.get(url, headers=headers, proxies=proxies)

    return response.text


