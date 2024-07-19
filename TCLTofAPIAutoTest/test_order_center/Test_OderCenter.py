# python3.10
# coding:utf-8
# @File : Test_OderCenter.py
# @Author : Andy
# @Date : 2024/7/9 10:40
# @Desc : # story：测试用例，测试场景，title：标题，替换test_query_po_list
# description: TCL新方舟DEV秘鲁账号，订单中心，接口自动化测试脚本
import glob
import json
import os
import yaml


import allure
import pytest
import requests

from lib.LoginDEV import login
from lib.read_yaml import read_yaml

# 调用公共登录方法，这里参数是秘鲁账号
login = login(url='https://tofobg-dev-gateway.eads.tcl.com/oauth/login?type=account&username=PEdongming2.zhang'
                  '&password=aEDyiJpMApmlb4h%2Bv0LJD8KoptUtluMChfrIgLU3GHo5sgemZikHMT'
                  '%2F1owZiRKF9IUg4p1QuAvlT8tBr4MIIcA%3D%3D&captcha= '
              )
# 带有token的请求头
headers = {"Authorization": login}
# 实列化读取yaml的对象，返回的data是一个列表，后续的测试用例根据序号和字典键取值
data_list = read_yaml("../lib/datas.yaml")
# fiddler代理
fiddler_proxies = {
    "http": "http://127.0.0.1:8888"
}


# 订单中心api测试类
class Test_OderCenter:
    # 查询po列表
    @allure.description('查询新建的po列表-测试用例描述')
    @allure.story('查询新建的po列表-测试用例场景')
    @allure.title('查询新建的po列表-测试用例标题')
    def test_queryPOList(self):
        url = data_list[0]["url1"]
        data = data_list[0]["data"]
        res = requests.post(url=url, json=data, headers=headers, proxies=fiddler_proxies,verify=False)
        # 返回的数据字符串转为字典
        po_dict = json.loads(res.text)
        assert po_dict["message"] == "success"

    # 查询订单状态是“草稿”的PO列表，取第列表的第一个PO号，返回PO号，方便后面的提交使用
    def query_po_list_for_submit(self) -> str:
        self.url = data_list[0]["url1"]
        self.data = data_list[0]["data"]
        self.res = requests.post(url=self.url, json=self.data, headers=headers)
        # 返回的数据字符串转为字典
        self.po_dict = json.loads(self.res.text)
        # 取出po号，给后面的提交接口使用
        self.custOrderNo = self.po_dict["data"]["content"][0]["custOrderNo"]
        # 返回po号
        return self.custOrderNo

    # 校验PO保存接口返回消息成功
    @allure.description('校验PO保存接口返回消息成功')
    @allure.story('校验PO保存接口返回消息成功')
    def test_POSave(self):
        url = data_list[1]["url2"]
        data = data_list[1]["data"]
        res = requests.post(url=url, json=data, headers=headers)
        po_dict = json.loads(res.text)
        assert po_dict["message"] == "success"

    # 校验PO提交接口返回200
    @allure.description('校验PO提交接口返回消息是success')
    @allure.story('校验PO提交接口返回消息是success')
    @allure.step('校验PO提交接口返回消息是success-测试步骤')
    def test_PoSubmit(self):
        url = data_list[2]["url3"]
        # po号从查询列表方法调过来
        data = [{"custOrderNo": Test_OderCenter.query_po_list_for_submit(self)}]
        res = requests.post(url=url, json=data, headers=headers)
        po_dict = json.loads(res.text)
        assert po_dict["message"] == "success"

    @allure.description('校验查询POPE24070200024详情接口返回code是success')
    def test_POInfo(self):
        url = data_list[3]["url4"]
        res = requests.get(url=url, headers=headers)
        po_dict = json.loads(res.text)
        # 断言响应 code == success
        assert po_dict["code"] == "success"

    @allure.description('校验导出POPE24053000002内容中包含[Content_Types].xml')
    def test_PoExport(self):
        url = data_list[4]["url5"]
        data = data_list[4]["data"]
        res = requests.post(url=url, json=data, headers=headers)
        #  断言[Content_Types].xml 在 响应的text中
        assert '[Content_Types].xml' in res.text

    @allure.description('校验importPO接口返回200')
    def test_PoImport(self):
        url = data_list[5]["url6"]
        res = requests.post(url=url, headers=headers)
        assert res.status_code == 200

    @allure.description("查询SO订单状态是“审核中”的SO列表，接口返回消息success表示请求成功")
    def test_QuerySOList(self):
        url = data_list[6]["url7"]
        data ={}
        res = requests.get(url=url,json=data, headers=headers)
        po_dict = json.loads(res.text)
        assert po_dict["message"] == "success"
    




