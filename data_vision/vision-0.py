# _*_coding:utf-8 _*_
# @Time　　:2019/7/17   14:46
# @Author　 : wy
# @ File　　  :vision-0.py
# @Software  :PyCharm
from random import seed, randint
from matplotlib import pyplot

x = [x for x in range(365)]
y = [randint(10000, 10200) for y in range(365)]
pyplot.plot(x, y)
# 线段图
pyplot.show()
