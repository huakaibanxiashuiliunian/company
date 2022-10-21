# -*- coding = utf-8 -*-
# @Time :  13:04
# @Author : XX
# @File : login.py
# @Software : PyCharm
import requests
from werkzeug.sansio.multipart import MultipartEncoder

import login


def upload(filepash,id):
    session, token, head = login.login()
    # 获取元数据
    id = str(id)
    url = "http://192.168.1.252/api?method=formData.get&entity=gjbz&lang=cn&id=%s&&"% id
    print(url)
    resp = requests.get(url=url, headers=head)
    print(resp.json())
    data1 = resp.json()
    #上传文件
    url = "http://192.168.1.252/form/uploadAttachment?type=file&_csrf=%s" % token
    data = open(filepash, 'rb')
    response = requests.post(url, files={'upload': data}, headers=head)
    print(response.json())
    data2 = response.json()

    attachment = {}
    attachment["name"] = data2["data"]["name"]
    attachment["url"] = data2["data"]["url"]
    print(attachment)
    # "{\"name\":\"DGTJ08-2064-2009地下铁建筑结构抗震设计规范.rar\",\"url\":\"/static/upload/attachment/20221020/92/165748148.rar\"}",
    attachment = str(attachment).replace("'",'"').replace('"','\"')
    # data1["data"]["attachments"] = attachment
    # print(data1)
    b = {
        "attachments": attachment,
        "id": data1["data"]["id"],
        "name": data1["data"]["name"],
        "type": data1["data"]["type"]["id"],
        "中国标准分类号": data1["data"]["中国标准分类号"],
        "发布日期": data1["data"]["发布日期"],
        "国际标准分类号": data1["data"]["国际标准分类号"],
        "实施日期": data1["data"]["实施日期"],
        "标准号": data1["data"]["标准号"],
        "标准类别": data1["data"]["标准类别"],
        "起草人": data1["data"]["起草人"],
    }
    print(b)
    # 提交文件
    url = "http://192.168.1.252/api?method=formData.update&entity=gjbz&_csrf=%s&lang=cn" % token
    resp = requests.post(url=url, data=b, headers=head)
    print(resp.json())
    print("提交数据库")
    session.close()







