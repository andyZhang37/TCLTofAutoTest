# python3.10
# coding:utf-8
# @File : 56.py
# @Author : Andy
# @Date : 2022/8/28 10:40
# @Desc :
# import requests

# # 要发送的数据
# data = {
#     'key1': 'value1',
#     'key2': 'value2'
# }
#
# # 发送POST请求
# response = requests.post('http://httpbin.org/post', data=data)
#
# # 打印响应内容
# print(response.text)
import requests

# url = 'https://tofobg-dev-gateway.eads.tcl.com/oauth/login?type=account&username=PEdongming2.zhang&password=aEDyiJpMApmlb4h%2Bv0LJD8KoptUtluMChfrIgLU3GHo5sgemZikHMT%2F1owZiRKF9IUg4p1QuAvlT8tBr4MIIcA%3D%3D&captcha='
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,  like Gecko) Chrome/126.0.0.0 Safari/537.36",
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "Content-Type": "application/x-www-form-urlencoded",
#     }
# data = {'username': 'PEdongmig2.zhang',
#         'password': 'TCL123456',
#         'captcha': '',
#         }

# session = requests.Session()
# response = requests.post(url=url )
# # list = response.history
# # print(list)
# # print(list[0].url)
# print(response.headers)
# print(response.url)
import json
user_info= '{"name" : "john", "gender" : "male", "age": 28}'
print(type(user_info))
user_dict = json.loads(user_info)

print(type(user_dict))
# {u'gender': u'male', u'age': 28, u'name': u'john'}