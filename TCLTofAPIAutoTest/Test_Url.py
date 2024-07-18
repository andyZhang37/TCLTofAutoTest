# python3.10
# coding:utf-8
# @File : 56.py
# @Author : Andy
# @Date : 2022/8/28 10:40
# @Desc : 读取yaml数据
import requests
import allure
import yaml
# from self import self


# 编写读取yaml数据函数,只能读取单行数据，读取多行数据报错
# def read_yaml(file_path):
#     with open(file_path, 'r',encoding='utf-8') as f:
#         return yaml.safe_load(f)
#
#
# # 编写读取yaml数据函数,可以读取多行数据
# def read_yaml2(file_path):
#     with open(file_path, 'r',encoding='utf-8') as f:
#         return yaml.safe_load_all(f.read())
#
#
# # 读取返回列表式结果
# def read_yaml3(file_path):
#     with open(file_path, 'r',encoding='utf-8') as f:
#         return list(yaml.safe_load_all(f.read()))


# 实列化
# data = read_yaml("../lib/datas.yaml")
# data3是一个列表
# data3 = read_yaml3("../lib/datas.yaml")
# print(data3[0]["url1"])
# print(data3[0]["data"])
# <generator object load_all at 0x00000261AE8B9850>
# for c in data3:
#     print(c)
# print(data2["key1"])


# data3 = read_yaml3("../lib/datas.yaml")
# print(data3)
# [{'name': 'zhangsan', 'age': 18}, {'name': 'lisi', 'age': 25}, {'name': 'wangwu', 'age': 33}, {'name': 'libai',
# 'age': 78}]
class Test_Url:
    @allure.description("访问百度")
    def test_url(self):
        url  = "https://www.baidu.com/"
        res = requests.get(url=url)
        print(res.status_code)

    def test(self):
        pass

    def test2(self):
        pass

    def test3(self):
        pass

    def test4(self):
        pass