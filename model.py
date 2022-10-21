# -*- coding = utf-8 -*-
# @Time :  16:40
# @Author : XX
# @File : jpgDownload.py
# @Software : PyCharm
import time
import urllib.request
from urllib import request, error
from urllib import parse
from selenium.webdriver import ChromeOptions
from Reptile_flask import cookie, company
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver

url = "http://192.168.1.252"
head = '''{
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37"
}'''

import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


def gethtml(url):       # # 调用webdriver模拟浏览器操作获取html页面并返回
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
        "cookie": cookie.companyCookie,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53"}
    html = ""
    try:
        req = urllib.request.Request(url, headers=head)
        resp = urllib.request.urlopen(req)
        # html = json.load(resp)
        html = resp.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def geturl(html):
    file = open("model.html", encoding='utf-8')  # 避免爬取过多被封 先提取页面到本地 之后注释

    bs = BeautifulSoup(file, "html.parser")
    data1 = bs.select("div.search-result-wrapper > ul > li>div>div>a")  # 找出详情
    data2 = bs.select(
        "div.search-result-wrapper > ul > li.search-result-item-wrapper > div >div.search-result-item-desc")
    result = {}
    product1 = []
    product2 = []
    product3 = []
    hrefs = {}
    for item in data1:
        name = item.get_text()
        item = str(item)
        href = item.replace("</a>","").replace(">","").replace("<a","").replace('="'," ").replace('"',' ').split()
        # hrefs.append(href[href.index("href")+1])
        hrefs[name]=href[href.index("href")+1]
        product1.append(name)
    for item in data2:
        name = item.get_text()
        product2.append(name)
    for i in range(0, len(product1)):
        result[product1[i]] = product2[i]
        product3.append(product1[i])
        product3.append(product2[i])
    return product1,product2,product3,hrefs


def getdata(html):
    # file = open("product.html", encoding='utf-8')  # 避免爬取过多被封 先提取页面到本地 之后注释

    bs = BeautifulSoup(html, "html.parser")
    data = bs.select("div.tech-specs-items-wrap>div.tech-specs-items-description-wrap>ul>li>span.tech-specs-items-description__title--heading")  # 找出详情
    result = {}
    product1 = []
    product2 = []
    product3 = []
    product4 = []
    for item in data:
        title = item.get_text()
        product1.append(title)
    for i in product1:
        if i not in product2:
            product2.append(i)
    print(product2)
    data = bs.select("div.tech-specs-items-wrap>div.tech-specs-items-description-wrap>ul>li")
    for item in data:
        title = item.get_text()
        product3.append(title)
        for a in product2:
            if a == item:
                continue
            result[a]=title
    for i in product3:
        if i not in product4:
            product4.append(i)
    print(product4)

def main():
    key = '杭州海康威视数字技术股份有限公司'
    guanwang = company.getofficialurl(key)
    print(guanwang)
    url = r"https://%s/cn/search/?q=" % guanwang
    key = '防爆网络摄像机'            # 主要搜索字段
    finalUrl = parse.quote(key)
    newurl = url + finalUrl  # 对关键字进行加密处理使浏览器识别

    # print(html)
    # html = askURL(url)
    html = gethtml(newurl)          # 调用webdriver模拟浏览器操作获取html页面并返回
    with open("model.html", "w", encoding='utf-8') as file:         # 缓存页面到本地
        file.write(html)
    product1,product2,product3,hrefs = geturl(html)        # product1  型号  product2 型号及描述   型号及链接[]类型      hrefs型号及链接{}类型
    print(product1)
    for href in hrefs:
        if key == href:
            newurl = url.replace("/cn/search/?q=","")+hrefs[href]
            print("-------------------查询%s--------------------"%key)
            print(newurl)
            html = gethtml(newurl)
            getdata(html)
        else:
            if len(product1) != 0:
                try:
                    newurl = url.replace("/cn/search/?q=", "") + hrefs[product1[0]]
                    print("-------------------查询%s--------------------"%href)
                    print(newurl)
                    html = gethtml(newurl)
                    getdata(html)
                except TypeError as e:
                    print(e)
            break

    # print(html)
if __name__ == "__main__":
    main()
