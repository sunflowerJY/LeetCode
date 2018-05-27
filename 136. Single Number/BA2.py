# -*- coding: utf-8 -*-
"""
@Time    : 2018/2/5 20:50
@Author  : Sunflower
@FileName: BA2.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""


from functools import reduce

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: x ^ y, nums)