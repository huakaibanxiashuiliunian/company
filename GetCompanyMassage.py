#coding:utf-8

import time
import redis

from Reptile_flask import operational_database, company

rc = redis.StrictRedis(host="192.168.1.252", port="6379", db=3, password="zh")
ps = rc.pubsub()
ps.subscribe("formData.create")    # 订阅消息
for item in ps.listen():        # 监听状态：有消息发布了就拿过来
    # print(item["data"])    # 消息的详细信息
    massage = str(item['data']).replace("b'{","").replace('"','').replace("}'","").replace(","," ").replace(":"," ").split()

    if "entity" in massage:
        name = massage[massage.index('entity')+1]
        if name == "obj_company":
            id = massage[massage.index('id')+1]
            if id != 1:
                try:
                    print("ID: "+id)   # 新创建了一个id为xx 的公司
                    companyName = operational_database.select_company(id)[0]
                    print("companyName: "+companyName)
                    company.update_mysql(companyName)
                except Exception as e:
                    print(e)