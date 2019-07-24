# _*_coding:utf-8 _*_
# @Time　　:2019/7/17   15:01
# @Author　 : wy
# @ File　　  :vision-2.py
# @Software  :PyCharm

from random import seed, randint
from matplotlib import pyplot
from numpy.matlib import randn

x = randn(1000)
pyplot.hist(x)
pyplot.show()