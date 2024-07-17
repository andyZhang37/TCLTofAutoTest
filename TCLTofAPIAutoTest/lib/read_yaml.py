# python3.10
# coding:utf-8
# @File : read_yaml.py
# @Author : Andy
# @Date : 2024/7/9 10:40
# @Desc : 读取yaml文件的公共方法，返回值是一个列表，YAML里面的数据格式是按照字典类型来存放
import yaml


def read_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return list(yaml.safe_load_all(f.read()))





