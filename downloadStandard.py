import datetime
import linecache
import os
import random
import urllib

import time
import zipfile
from Reptile_flask import cookie

import requests
from unrar import rarfile



downurl = "http://down.bzmfxz.com/201407/20140703GB/GB1094.12013.rar"
filename = "GB1094.12013.rar"
filedir = "GB1094.12013"
def downLoad(downurl,filedir):
    filename = filedir + ".rar"
    print(filedir)
    print(filename)
    session = requests.Session()
    # a = random.randrange(1, 100)  # 1-100中生成随机数
    # # 从文件poem.txt中对读取第a行的数据
    # proxyip = linecache.getline(r'IP代理池.txt', a).replace(" ", "").replace("':", "").replace("'", " ").split()
    # print(proxyip[proxyip.index("HTTP") + 1])
    # proxy = proxyip[proxyip.index("HTTP") + 1]
    # proxyip = {'HTTP': proxy}
    # headers = {"user-agent": cookie.user_agent2,
    #            "cookie": cookie.downCookie}
    # # # session.proxies = proxyip
    print("访问首页")
    response = session.get(url='http://www.bzmfxz.com')
    print("成功访问首页")
    time.sleep(5)
    print(datetime.datetime.now())
    print("开始下载")
    try:
        response2 = session.get(downurl)
        if os.path.exists("D:\Download"):
            pass
        else:
            os.mkdir("D:\Download")
        with open("D:\Download\%s" % filename, "wb") as f:
            print("保存文件")
            f.write(response2.content)
            print("文件保存位置: D:\Download\%s" % filename)
            print("下载成功")
    except Exception as e:
        print("下载失败")
        print(e)
    finally:
        session.close()
        # session.invalidate()
    print(datetime.datetime.now())
    # decompression(filename,filedir)     # 解压文件
    '''
    基本格式：zipfile.ZipFile(filename[,mode[,compression[,allowZip64]]])
    mode：可选 r,w,a 代表不同的打开文件的方式；r 只读；w 重写；a 添加
    compression：指出这个 zipfile 用什么压缩方法，默认是 ZIP_STORED，另一种选择是 ZIP_DEFLATED；
    allowZip64：bool型变量，当设置为True时可以创建大于 2G 的 zip 文件，默认值 True；
    '''


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
    downLoad(downurl, filename)
    pass