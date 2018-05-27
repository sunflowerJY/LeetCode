# -*- coding: utf-8 -*-
"""
@Time    : 2018/2/3 21:25
@Author  : Sunflower
@FileName: BA.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""


class Solution:
    def hasAlternatingBits(self, n):
        return '00' not in bin(n) and '11' not in bin(n)