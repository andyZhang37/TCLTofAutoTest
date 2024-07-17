# python3.10
# coding:utf-8
# @File : LoginDEV.py
# @Author : Andy
# @Date : 2022/8/28 10:40
# @Desc : 登录新方舟的公共方法
import requests


# class LoginTof:

# 登录DEV（开发环境）亚太新方舟系统
def login(url):
    #  url拼接,访问这个URL，登录重定向返回的第二个location才会有token
    response = requests.post(url=url)
    # print(response.headers)
    # print(response.url)
    # 后续请求头中带这这个Authorization: bearer 365db221-7c0a-4bb5-aad7-d6a031181753
    return "bearer " + response.url[54:90]



# if __name__ == "__main__":

    # 调用方法获取token
# login = login()
# print(login)
