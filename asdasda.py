# -*- coding = utf-8 -*-
# @Time :  13:12
# @Author : XX
# @File : asdasda.py
# @Software : PyCharm

a = {'code': 1, 'data': {'id': '99a7a4c7-6988-4700-9410-8008ecf215eb', 'createTime': '2022-10-21T01:26:34.356Z', 'mimetype': 'application/octet-stream', 'path': '/var/www/html/ipowerone/upload/attachment/20221021/92/092634296.rar', 'sign': '24acdbe790b194e16ba5b2a39e1f04d1', 'url': '/static/upload/attachment/20221021/92/092634296.rar', 'size': 972575, 'name': 'GB7260.2-2009不间断电源设备(ups)第2部分电磁兼容性(emc)要求.rar', 'createUser': {'id': 92, 'name': 'api002', 'realName': None, 'username': 'api002', 'headimg': None, 'sex': None, 'sign': None, 'password': 'e1b5f0eccdb69a932b28c7bbd6cfef9ab1cf48591f36aa203860d3cae3e0161d', 'email': '', 'mobile': '', 'mobileValidated': 0, 'address': '', 'company': '', 'position': '', 'status': 2, 'data': {}, 'birthday': None, 'age': None, 'city': None, 'intro': None, 'loginTime': '2022-10-21T05:00:40.000Z', 'loginIp': '192.168.1.106', 'lastLoginTime': '2022-10-21T04:57:39.000Z', 'lastLoginIp': '192.168.1.106', 'session': '5hYqwUj-HjcC1QGS5tiUG1dQRIN7hzo_', 'isSSO': True, 'activeTime': '2022-10-21T02:57:46.000Z', 'online': 1, 'updatedAt': '2022-10-21T05:00:40.000Z', 'createdAt': '2022-09-27T03:18:08.385Z'}}, 'message': '上传成功', 'uploaded': 1, 'url': '/static/upload/attachment/20221021/92/092634296.rar'}
print(a["data"]["url"])
print(a["data"]["name"])
attachment = {}
attachment["name"]=a["data"]["name"]
attachment["url"]=a["data"]["url"]
print(attachment)
b = {
"attachments": "{\"name\":\"DGTJ08-2064-2009地下铁建筑结构抗震设计规范.rar\",\"url\":\"/static/upload/attachment/20221020/92/165748148.rar\"}",
"id": "566",
"name": "电力变压器 第1部分：总则",
"type": "1",
"中国标准分类号": "null",
"发布日期": "null",
"国际标准分类号": "null",
"实施日期": "null",
"标准号": "GB  1094.1-2013",
"标准类别": "null",
"起草人": "null"
}

c = {'code': 1, 'data': {'id': '566', 'attachments': {'name': 'DGTJ08-2064-2009地下铁建筑结构抗震设计规范.rar', 'url': '/static/upload/attachment/20221020/92/165748148.rar'}, '中国标准分类号': None, '发布日期': None, '标准号': 'GB  1094.1-2013', '标准类别': None, '实施日期': None, 'name': '电力变压器 第1部分：总则', '起草人': None, '国际标准分类号': None, 'type': {'id': '1', 'name': '行业标准'}}}


a = "{'name': 'GB7260.2-2009不间断电源设备(ups)第2部分电磁兼容性(emc)要求.rar', 'url': '/static/upload/attachment/20221021/92/092634296.rar'}"
print(a.replace("'",'"').replace('"','\\"'))
b = "{\"name\":\"DGTJ08-2064-2009地下铁建筑结构抗震设计规范.rar\",\"url\":\"/static/upload/attachment/20221020/92/165748148.rar\"}"