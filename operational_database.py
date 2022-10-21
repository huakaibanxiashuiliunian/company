# -*- coding = utf-8 -*-
# @Time :  16:40
# @Author : XX
# @File : jpgDownload.py
# @Software : PyCharm

import pymysql
import datetime

from sympy.parsing.sympy_parser import null

# 数据库配置
host = "192.168.1.252"
user = "root"
password = 'tekinfo119TOPower'
port = 3306
database = "ipower_carrier"


def main():
    name = select_datasheet(472)
    print(name[0])
    pass


def select_company(id):
    try:
        conn = pymysql.connect(host=host, user=user, password=password, port=port, database=database)  # 连接mysql
        cur = conn.cursor()  # 获取游标
        print("------------------------------数据库连接成功------------------------------")
        time = datetime.datetime.now()
        count = cur.execute("select name from obj_company where id = '%s'" % id)  # 查看数据库是否有该数据
        if count != 0:
            name = cur.fetchone()
        else:
            return "没有ID为%s的数据"%id
    except pymysql.Error as e:
        print("数据库连接失败")
        conn.rollback()
    finally:
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接
        print("-----------------------------关闭数据库连接------------------------------")
    return name

def select_datasheet(id):      # 根据id查询标准号，标准名称
    try:
        conn = pymysql.connect(host=host, user=user, password=password, port=port, database=database)  # 连接mysql
        cur = conn.cursor()  # 获取游标
        time = datetime.datetime.now()
        count = cur.execute("select 标准号,name from obj_gjbz where id = '%s'" % id)  # 查看数据库是否有该数据
        if count != 0:
            name = cur.fetchone()   # 将查询结果赋值给name
            return name
        else:
            return "没有ID为%s的数据"%id
    except pymysql.Error as e:
        print("数据库连接失败")
        conn.rollback()
    finally:
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接
        print("-----------------------------查询%s标准号和标准名称------------------------------" % id)

def save_mysql(id,resource):
    try:
        conn = pymysql.connect(host=host, user=user, password=password, port=port, database=database)  # 连接mysql
        cur = conn.cursor()  # 获取游标
        print("------------------------------数据库连接成功------------------------------")
        time = datetime.datetime.now()
        count = cur.execute("select name from obj_company where id = '%s'" % id)  # 查看数据库是否有该数据

        if count != 0:
            # 存在   更新数据库的sql
            updateSql = '''
            update obj_company set address='%s',website='%s',bankAccountName='%s',createDate='%s',no='%s',法人='%s',公司邮箱='%s',公司电话='%s'  where name='%s'
            ''' % (resource.get("地址"), resource.get("官网"), resource.get("单位名称"),
                   datetime.datetime.now(), resource.get("统一社会信用代码"), resource.get("法定代表人"),
                   resource.get("邮箱"), resource.get("电话"), resource.get("单位名称"))
            print(updateSql)
            print(time)
            cur.execute(updateSql)  # 执行sql
            conn.commit()  # 向数据库提交
            print("-----------------------------数据更新成功------------------------------")
        else:
            pass
    except pymysql.Error as e:
        print("数据更新失败,该公司已存在！！！: " + str(e))
        conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 关闭连接
    print("-----------------------------关闭数据库连接------------------------------")


def mysql(id):      # 测试方法
    try:
        conn = pymysql.connect(host=host, user=user, password=password, port=port, database=database)  # 连接mysql
        cur = conn.cursor()  # 获取游标
        time = datetime.datetime.now()
        count = cur.execute("select 标准号,name from obj_gjbz where id = '%s'" % id)  # 查看数据库是否有该数据
        # print(cur.fetchone())
        if count != 0:
            name = cur.fetchone()
        else:
            return "没有ID为%s的数据"%id
    except pymysql.Error as e:
        print("数据库连接失败")
        conn.rollback()
    finally:
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接
        print("-----------------------------查询%s标准号------------------------------" % id)
    return name


if __name__ == "__main__":
    # main()
    key = mysql(34)
    print(key)
    standardnumber = str(key[0])
    standardname = str(key[1])
    print(standardname)
    print(standardnumber)