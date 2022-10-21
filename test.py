# -*- coding = utf-8 -*-
# @Time:2022/9/19 10:14
# @Author : XX
# @File : spider.py
# @Software : PyCharm
import datetime
import linecache
import multiprocessing
import os
import queue
import random
import time
import zipfile

import requests
# from random import random

from unrar import rarfile

def aa():
    url = "https://movie.douban.com/top250"
    uchar = "YD T 5186-2010"
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        print("您输入的是汉字")
    else:
        print("不是汉字")
    print(type(None))


def jieya():
    filename = "YDT1184-2002接入网电源技术要求.rar"
    filedir = "D:\Download"
    print("开始解压文件")
    rar = rarfile.RarFile("D:\Download\%s" % filename)
    # 解压缩到指定目录
    rar.extractall(filedir)
    print("解压成功")


def get_user_agent():
    '''
    随机获取一个用户代理
    '''
    user_agents=[
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
    ]
    # random.choice返回列表的随机项
    user_agent = random.choice(user_agents)
    return user_agent

    # random.randint产生随机整数
    time.sleep(2 + float(random.randint(1, 100)) / 20)


def bb():
    url_search = "http://www.bzmfxz.com"
    session = requests.Session()
    cookies = session.get(url_search).cookies.get_dict()
    print(cookies)

    session.close()
    session.invalidate()



downurl = "http://www.down.bzmfxz.com/GJBZ/41/GB-T1094.4-2005.rar"
filename = "GB-T1094.4-2005.rar"
filedir = "GB-T1094.4-2005"
def downLoad(downurl,filedir):
    filename = filedir + ".rar"
    session = requests.Session()
    print("访问首页")
    response = session.get('http://www.bzmfxz.com')
    print("成功访问首页")
    time.sleep(5)
    print(datetime.datetime.now())
    print("开始下载")
    try:
        response2 = session.get(downurl).content
        if os.path.exists("D:\Download"):
            pass
        else:
            os.mkdir("D:\Download")
        with open("D:\Download\%s" % filename, "wb") as f:
            f.write(response2)
            print("下载成功")
    except Exception as e:
        print("下载失败")
        print(e)
    finally:
        session.close()
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


def bbb():
    import pandas as pd
    import re
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from dateutil.relativedelta import relativedelta

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    path = (r'C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe')
    opener = webdriver.Chrome(executable_path=path)  # 打开谷歌浏览器
    opener.maximize_window()  # 设置全屏
    # opener = webdriver.Chrome(chrome_options=chrome_options)
    opener.get('http://skykeyeb.ez-wms.com/')  # 输入易仓网址打开易仓
    opener.find_element_by_xpath('//*[@id="userName"]').send_keys('xxxx')  # 输入登录的账号
    opener.find_element_by_xpath('//*[@id="userPass"]').send_keys('mmm')  # 输入登录的密码
    opener.find_element_by_xpath('//*[@id="login"]').click()  # 点击登录
    time.sleep(5)  # 等待 5 秒
    # 自动获取cookie
    cookies = opener.get_cookies()
    name_pat = "'name':.'(.*?)'"
    value_pat = "'value':.'(.*?)'"
    value = re.compile(value_pat).findall(str(cookies))
    name = re.compile(name_pat).findall(str(cookies))
    opener.quit()
    cookie_result = ''
    for i in range(len(name)):
        opener.quit()
        cookie_result = cookie_result + name[i] + '=' + value[i] + ';'
    print(cookie_result)

queue = multiprocessing.Queue(10)
def write_queue():
    i = 0
    while True:
        queue.put(i)
        time.sleep(1)
        i = i+1


def read_queue():
    while True:
        print(queue.get())

def aaaaaaa():
    p1 = multiprocessing.Process(target=write_queue(),args=(queue,))
    p1.start()
    p1.join()
    p2 = multiprocessing.Process(target=read_queue(),args=(queue,))
    p2.start()
    p2.join()

if __name__ == "__main__":
    # keyList = ['GB T 28827.1-2012','GB T 28827.2-2012','GB T 28827.3-2012','GB T 24405.1-2009','GB T 24405.2-2010','GB t 4754-2017','GB 1094.1-2013','GB 1094.2-2013','GB 1094.2-2013','GB 13028-91','GB 1094.5-2008','CECS 115：2000','DL T 985-2005','GB T 10228-2008','GB 24790-2009','GB T 17468-2008','GB T 1094.4-2005','GB T 1094.10-2003','GB T 10228-2008','JB T 10217-2000','GB 50054-95','GB 7251.1-2005','GB 7251.2-2006','GB 10963.2-2008','GB 12706.3-91','GB 13539.1-2015','GB 14048.1-2006','GB 14048.2-2008','GB 14048.3-2008','GB T 12706.1-4-2002','GB T 15408-2011']
    # for i in keyList:
    #     downLoad(i)
    # a = random.randrange(1, 100)  # 1-100中生成随机数
    # # 从文件poem.txt中对读取第a行的数据
    # proxyip = linecache.getline(r'IP代理池.txt', a)
    # print(proxyip)
    aaaaaaa()