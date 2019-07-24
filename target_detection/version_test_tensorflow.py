#  _*_ coding:UTF-8 _*_
# 查看tensorflow是什么版本
import os
from tensorflow.python.client import device_lib
import tensorflow as tf

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "99"

if __name__ == "__main__":
    print(device_lib.list_local_devices())
    print(tf.__version__)
