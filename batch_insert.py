# _*_coding:utf-8 _*_
# @Time　　:2019/7/22   10:30
# @Author　 : wy
# @ File　　  :batch_insert.py
# @Software  :PyCharm
# -*- coding:utf-8 -*-
import time
from pymysql import *


# 装饰器，计算插入50000条数据需要的时间
def timer(func):
    def decor(*args):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        d_time = end_time - start_time
        print("the running time is : ", d_time)

    return decor


@timer
def add_test_users():
    conn = connect(host='localhost', port=3306, user='wengxh', password='mysql', database='school', charset='utf8')
    cs = conn.cursor()  # 获取游标
    # print(cs)
    for num in range(0, 58000):
        try:
            sql = "insert into person (name,age,address) values ('zhangsan','19','上海市')"
            cs.execute(sql)

        except Exception as e:
            print(e)
            return

    conn.commit()  # 提交
    cs.close()
    conn.close()
    print('OK')


add_test_users()
