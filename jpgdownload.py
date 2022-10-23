# -*- coding = utf-8 -*-
# @Time :  16:40
# @Author : XX
# @File : jpgDownload.py
# @Software : PyCharm
import datetime
import re
from urllib import request, error, parse
import time

import requests
from bs4 import BeautifulSoup
from pythonProject import cookie, downloadStandard
import Levenshtein

# 得到一个指定url的网页
def askURL(url):
    head = {
        "user-agent": cookie.user_agent}
    html = ""
    i = 0
    while i < 5:        # 超时重连  五次
        try:
            html = requests.get(url=url, headers=head, timeout=20).text
            print(time.strftime('%Y-%m-%d %H:%M:%S'))
            return html
        except Exception as e:
            i += 1
            print("连接超时，尝试重新连接 ")
            if i == 5:
                return ""       # 失败五次 返回空字符


def geturl1(html):
    bs = BeautifulSoup(html, "html.parser")
    data = bs.select("ul", class_="cl")
    urllist = []
    for item in data:
        item = item.find_all("img")
        for i in item:
            url = str(i).replace("="," ").replace('"',"").split()
            url = str(url[url.index("lazysrc")+1]).replace(".278.154.jpg","")
            urllist.append(url)
    return urllist


def downloadpng(url):
    head = {
        "user-agent": cookie.user_agent
    }
    name = url.replace("https://pic.3gbizhi.com/","").split("/")
    name = name[len(name)-1]
    print(name)
    jpg = requests.get(url=url, headers=head).content
    with open(r"D:\JPGDOWNLOAD\%s" % name, "wb") as file:
        file.write(jpg)
        print(time.strftime('%Y-%m-%d %H:%M:%S'))



def biaozhun(url):
    start = datetime.datetime.now()
    print(start)
    html = askURL(url)
    if html.strip() == "":
        print("获取页面失败")
    else:
        urllist = geturl1(html)
        for url in urllist:
            print(url)
            downloadpng(url)



if __name__ == "__main__":
    url = "https://desk.3gbizhi.com/deskMV/"
    biaozhun(url)

