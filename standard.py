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
from selenium.webdriver import ChromeOptions
from selenium import webdriver
from Reptile_flask import cookie, downloadStandard
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import Levenshtein
from Reptile_flask import uploadFile


# 数据库配置
host = "192.168.1.252"
user = "root"
password = 'tekinfo119TOPower'
port = 3306
database = "ipower_carrier"


def gethtml(url):  # # 调用webdriver模拟浏览器操作获取html页面并返回
    # 设置options参数，以开发者模式运行
    option = ChromeOptions()
    option.add_experimental_option("excludeSwitches", ["enable-automation"])

    # 解决报错，设置无界面运行
    option.add_argument('--no-sandbox')
    option.add_argument('--disable-dev-shm-usage')
    option.add_argument('window-size=1920x3000')  # 指定浏览器分辨率
    option.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    option.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
    option.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    option.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    # option.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"  # 手动指定使用的浏览器位置

    # 创建一个browser对象，模拟开启浏览器

    browser = webdriver.Chrome(options=option)  # 调用webdriver模拟浏览器操作，不显示浏览器执行过程      对于chromedriver.exe驱动，
    # 我已将chromedriver.exe 存放的目录添加到环境变量中了 D:\Google\Chrome\Application\  'D:\Google\Chrome\Application\chromedriver.exe'
    # browser = webdriver.Chrome()        # 浏览器显示执行
    browser.get(url)
    time.sleep(1)
    html = browser.page_source
    browser.close()
    return html





# 得到一个指定url的网页
def askURL(url):
    head = {
        "cookie": cookie.biaozhunCookie,
        "user-agent": cookie.user_agent}
    html = ""
    i = 0
    while i < 5:        # 超时重连  五次
        try:
            # req = urllib.request.Request(url, headers=head)
            # resp = urllib.request.urlopen(req,timeout=15)
            # # html = json.load(resp)

            html = requests.get(url=url,headers=head,timeout=15).text
            print(time.strftime('%Y-%m-%d %H:%M:%S'))
            return html
        except Exception as e:
            i += 1
            print("连接超时，尝试重新连接 ")
            print(time.strftime('%Y-%m-%d %H:%M:%S'))
            if i == 5:
                return ""       # 失败五次 返回空字符

def geturl1(html, key):
    bs = BeautifulSoup(html, "html.parser")
    # print(bs)
    data = bs.select("div.c_content>a")
    resource = {}
    downList = []
    standardName = []
    if not data:
        print("未找到%s" % key)
        a = "未找到%s" % key
        return a
    else:
        for item in data:
            print(item.get_text())
            a = item.get_text().replace(" ", "").replace("/", "")
            standardName.append(a)
            item = str(item).replace("</", "").replace("<", "").replace(">", "").replace("=", " ").replace('"',
                                                                                                           ' ').split()
            downloadurl = str(item[item.index('href') + 1])
            downList.append(downloadurl)
            resource[a] = downloadurl
            # print(downloadurl)
            # return downloadurl, filedir
        return resource,standardName

def geturl2(html, key):
    bs = BeautifulSoup(html, "html.parser")

    data = bs.select("div.c_content_overflow>a")
    resource = {}
    dataList = []
    if not data:
        print("未找到%s" % key)
        a = "未找到%s" % key
        return a
    else:
        for item in data:
            print(item.get_text())
            item = str(item).replace("</", "").replace("<", "").replace(">", "").replace('(', '').replace(")",
                                                                                                          "").replace(
                "'", " ").replace('"', ' ').split()
            downloadurl = str(item[item.index('window.open') + 1])
            # print(downloadurl)
            return downloadurl


def geturl3(html, key):
    bs = BeautifulSoup(html, "html.parser")
    # print(bs)
    data = bs.select("div[id='content']")
    resource = {}
    dataList = []
    if not data:
        print("未找到%s" % key)
        a = "未找到%s" % key
        return a
    else:
        for item in data:
            item = item.select("a")
            item = str(item).replace("</", "").replace("<", "").replace(">", "").replace('"',"").replace("="," ").split()
            downloadurl = str(item[item.index('href') + 1])
            # print(downloadurl)
            return downloadurl


def biaozhun(key,id):
    start = datetime.datetime.now()
    print(start)
    print("------------查询%s---------------" % key)
    url = "http://www.bzmfxz.com/search.aspx?searchtype=0&Keyword="
    if key >= u'\u4e00' and key<=u'\u9fa5':   # 判断是标准号还是标准名称
        newkey = parse.quote(key)       # 对标准名称进行加密
    else:
        # newkey = key.replace(" ", "%20")        # 对标准号中间的空格处理
        newkey = re.sub('[a-zA-Z]', '', key).replace("/","").replace(" ","")

    newUrl = url + newkey
    print(newUrl)
    html = askURL(newUrl)
    if html.strip() == "":
        print("获取页面失败")
    else:
        try:
            resource, standardName = geturl1(html, key)
            x = process.extractOne(key, standardName, scorer=fuzz.ratio)
            down = resource[x[0]]
            filedir = x[0]
            print(down)
        except Exception as e:
            print(e)
            down = "未找到%s" % key
        a = "未找到%s" % key
        if down == a:   # 未找到详细信息
            print(a)
        else:
            newUrl = url.replace("/search.aspx?searchtype=0&Keyword=", "") + down
            print(newUrl)
            html = askURL(newUrl)
            down = geturl2(html, key)
            if down == a:       # 未找到详细信息
                print(a)
            else:
                newUrl = url.replace("/search.aspx?searchtype=0&Keyword=", "") + down.replace("amp;", "")
                print(newUrl)
                newhtml = askURL(newUrl)
                # print(html)
                downurl = geturl3(newhtml, key)
                if downurl == a:       # 未找到详细信息
                    print(a)
                else:
                    downloadStandard.downLoad(downurl,filedir)      # 下载并解压缩  当前无解压
        end = datetime.datetime.now()
        print(end)
        filepash = "D:/Download/" + str(filedir) + ".rar"
        print(filepash)
        # 如果文件大小超过80k则下载成功
        uploadFile.upload(filepash, id)  # 调用接口更新数据库
        # 删除源文件   待完成


if __name__ == "__main__":
    # biaozhun("YD 5126-2005")
    # biaozhun("GB 7251.2-2006")
    # biaozhun("CECS 189-2005")
    biaozhun("YD /T 1363.4-2005","575")
    # biaozhun("通信系统用室外机柜安装设计规定")

'''http://www.bzmfxz.com/Common/ShowDownloadUrl.aspx?urlid=0&id=13720'''
