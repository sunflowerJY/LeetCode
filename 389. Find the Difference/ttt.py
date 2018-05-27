# -*- coding: utf-8 -*-
"""
@Time    : 2018/2/15 9:56
@Author  : Sunflower
@FileName: ttt.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""
from collections import Counter

c = Counter(['a', '2', '2', 'b', 'a', 'd', 'a'])

print(list(c.elements()))