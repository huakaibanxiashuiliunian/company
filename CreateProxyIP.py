# -*- coding = utf-8 -*-
# @Time :  13:58
# @Author : XX
# @File : CreateProxyIP.py
# @Software : PyCharm
import requests

from Reptile_flask import IPProxyPool


# 检查IP的可用性
def check_ip(list_ip):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71',
        'Connection': 'close'}
    # url = 'https://www.baidu.com'  # 以百度为例，检测IP的可行性
    url = 'https://movie.douban.com/subject/1292052/'

    can_use = []
    for ip in list_ip:
        try:
            response = requests.get(url=url, headers=headers, proxies=ip, timeout=3)  # 在0.1秒之内请求百度的服务器
            if response.status_code == 200:
                can_use.append(ip)
        except Exception as e:
            print(e)

    return can_use

def CreateProxyIPTXT():
    can_use = check_ip(IPProxyPool.GetProxyIP())
    print('能用的代理IP为：', can_use)
    # for i in can_use:
    #     print(i)
    print('能用的代理IP数量为：', len(can_use))

    fo = open('IP代理池.txt', 'w')
    for i in can_use:
        fo.write(str(i) + '\n')
    fo.close()


if __name__ == "__main__":
    CreateProxyIPTXT()