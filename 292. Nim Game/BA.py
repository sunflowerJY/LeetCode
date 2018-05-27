# -*- coding: utf-8 -*-
"""
@Time    : 2018/2/4 13:55
@Author  : Sunflower
@FileName: BA.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""


class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return False if not n % 4 else True