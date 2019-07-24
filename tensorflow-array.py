# _*_coding:utf-8 _*_
# @Time　　:2019/7/22   13:55
# @Author　 : wy
# @ File　　  :tensorflow-array.py
# @Software  :PyCharm
import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
m1 = tf.constant([[3, 3]])
m2 = tf.constant([[2], [3]])

product = tf.matmul(m1, m2)

print(product)

sess = tf.compat.v1.Session()

result = sess.run(product)
print(result)

sess.close()
