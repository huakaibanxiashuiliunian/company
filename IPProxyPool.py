# -*- coding = utf-8 -*-
# @Time :  13:45
# @Author : XX
# @File : IPProxyPool.py
# @Software : PyCharm
import requests
from bs4 import BeautifulSoup
import time


def GetProxyIP():
    list_ip = []
    list_port = []
    list_headers_ip = []

    for start in range(1, 11):

        url = 'https://www.kuaidaili.com/free/inha/{}/'.format(start)  # 每页15个数据，共爬取10页
        print("正在处理url: ", url)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71'}
        response = requests.get(url=url, headers=headers)

        soup = BeautifulSoup(response.text, 'html.parser')

        ip = soup.select('#list > table > tbody > tr > td:nth-child(1)')
        port = soup.select('#list > table > tbody > tr > td:nth-child(2)')

        for i in ip:
            list_ip.append(i.get_text())

        for i in port:
            list_port.append(i.get_text())

        time.sleep(1)  # 防止爬取太快，数据爬取不全

    # 代理ip的形式:        'http':'http://119.14.253.128:8088'

    for i in range(150):
        IP_http = 'http://{}:{}'.format(list_ip[i], list_port[i])
        IP_https = 'https://{}:{}'.format(list_ip[i], list_port[i])
        proxies = {
            'HTTP': IP_http,
            'HTTPS': IP_https
        }
        list_headers_ip.append(proxies)
        # print(proxies)

    print(list_headers_ip)
    return list_headers_ip

