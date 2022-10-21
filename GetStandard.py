# -*- coding = utf-8 -*-
# @Time :  11:37
# @Author : XX
# @File : GetStandard.py
# @Software : PyCharm
import redis
from concurrent.futures import ThreadPoolExecutor
from Reptile_flask import operational_database,  standard
import uploadFile

rc = redis.StrictRedis(host="192.168.1.252", port="6379", db=3, password="zh")
ps = rc.pubsub()
ps.subscribe("formData.create")    # 订阅消息
thread_pool = ThreadPoolExecutor(max_workers=2)   # 创建线程池 有三个线程
try:
    for item in ps.listen():  # 监听状态：有消息发布了就拿过来
        # print(item["data"])    # 消息的详细信息
        massage = str(item['data']).replace("b'{", "").replace('"', '').replace("}'", "").replace(",", " ").replace(":", " ").split()
        # print(massage)
        if "entity" in massage:
            name = massage[massage.index('entity')+1]
            if name == "obj_gjbz":
                print(massage)
                id = massage[massage.index('id')+1]
                if id != 1:
                    try:
                        print("ID: "+id)   # 新创建了一个id为xx 的标准
                        standardnumber = operational_database.select_datasheet(id)[0]       # 从数据库查询标准号
                        standardname = operational_database.select_datasheet(id)[1]         # 标准名称
                        print("标准号: "+str(standardnumber))
                        print("标准名称: "+str(standardname))
                        if standardnumber != None:
                            # keyandId = []
                            # keyandId.append(str(standardnumber))
                            # keyandId.append(str(id))
                            # thread_pool.submit(standard.biaozhun,keyandId)     # 从线程池开启一个线程(方法名，传入的参数)
                            standard.biaozhun(key=standardnumber,id=id)
                        else:
                            # standard.biaozhun(standardname)
                            pass

                    except Exception as e:
                        print(e)
except Exception as e:
    print(e)
                # company.update_mysql(standardnumber)