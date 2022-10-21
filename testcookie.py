# -*- coding = utf-8 -*-
# @Time :  14:57
# @Author : XX
# @File : testcookie.py
# @Software : PyCharm
import datetime
import linecache
import os
import random
import time

import requests
from unrar import rarfile


import requests
def login():
    login_url = 'http://www.bzmfxz.com'
    try:
        res = requests.get(url=login_url)
        cookies = res.cookies.items()
        print(cookies)
        cookie = ''
        for name, value in cookies:
            cookie += '{0}={1};'.format(name, value)
        return cookie
    except Exception as err:
        print('获取cookie失败：\n{0}'.format(err))

'''IISSafeDogLGSession=55C4C07CE25341B5607F6318E950DA09'''
'''IISSafeDogLGSession=55C4C07CE25341B5607F6318E950DA09'''
downurl = "http://down.bzmfxz.com/201412/20141210GB/GBT28827.22012.rar"
filename = "GBT28827.2-2012.rar"
filedir = "GBT28827.2-2012"
def downLoad(downurl,filedir):
    filename = filedir + ".rar"
    session = requests.Session()
    a = random.randrange(1, 100)  # 1-100中生成随机数
    # 从文件poem.txt中对读取第a行的数据
    proxyip = linecache.getline(r'IP代理池.txt', a).replace(" ","").replace("':","").replace("'"," ").split()
    print(proxyip[proxyip.index("HTTP")+1])
    proxy = proxyip[proxyip.index("HTTP")+1]
    proxyip = {'HTTP': proxy}
    session.proxies = proxyip
    print("访问首页")
    response = session.get('http://www.bzmfxz.com')
    print(session.headers)
    print("成功访问首页")
    time.sleep(5)
    print(datetime.datetime.now())
    print("开始下载")
    try:
        # cookie = login()
        # print(cookie)
        response = session.get(downurl).content
        print(session.headers)
        if os.path.exists("D:\Download"):
            pass
        else:
            os.mkdir("D:\Download")
        with open("D:\Download\%s" % filename, "wb") as f:
            f.write(response)
            print("下载成功")
            f.close()
    except Exception as e:
        print("下载失败")
        print(e)
    finally:
        pass
        # session.invalidate()
    print(datetime.datetime.now())
    decompression(filename,filedir)     # 解压文件



def decompression(filename,filedir):        # 解压缩方法
    try:
        filedir = "D:\Download\%s"%filedir
        print("开始解压文件")
        rar = rarfile.RarFile("D:\Download\%s" % filename)      # 读取文件
        # 解压缩到指定目录
        rar.extractall(filedir)
        print("解压成功")
        print("文件保存位置: %s" % filedir)
    except Exception as e:
        print("解压失败")
        print(e)


if __name__ == "__main__":
    downLoad(downurl,filedir)