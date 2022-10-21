# -*- coding = utf-8 -*-
# @Time :  13:04
# @Author : XX
# @File : login.py
# @Software : PyCharm
import requests
from hashlib import md5
def login():
    session = requests.Session()
    resp = str(session.get("http://192.168.1.252/api?method=api.getCsrfToken").content)
    # print(resp)     #    '''{"code":1,"data":"u1AE7IfG-0FR-oUb20c5sHZQvGapaVlGaBow"}'''
    _csrf = resp.replace("b'{","").replace("}'","").replace(","," ").replace(":","").replace('"'," ").split()
    token = _csrf[_csrf.index("data")+1]
    print(token)
    # print(_csrf)
    # print(session.cookies)
    url = "http://192.168.1.252/login"
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36X-Requested-With: XMLHttpRequest"
    }
    resp1 = session.get(url=url,headers=head)
    # print(session.cookies.items())
    cookie = str(session.cookies.items()).replace("[(","").replace("]"," ").replace("(","").replace(")","").replace("'","").replace(",","").split()
    _csrf = cookie[cookie.index("_csrf")+1]
    zhsid = cookie[cookie.index("zh-sid")+1]
    cookie = "_csrf="+_csrf+"; "+"zh-sid="+zhsid
    print(cookie)
    with open("Cookies.txt","w")as file:
        file.write(cookie)

    cookie = open("Cookies.txt","r").read()
    # print(cookie)
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36X-Requested-With: XMLHttpRequest",
        "Cookie": cookie
    }
    passwprd = "Test001."
    passwprd = md5(passwprd.encode('utf8')).hexdigest()
    data = {
        "username": "api002",
        "password": passwprd,
        # "captcha": "sdf"
    }
    url = url.replace("/login","/api?method=user.login")+"&_csrf=%s&lang=cn"%token
    print(url)
    request = session.post(url, data=data, headers=head)
    print(request.status_code)
    print("登录成功")
    return session,token, head
