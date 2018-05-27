# -*- coding: utf-8 -*-
"""
@Time    : 2018/2/5 20:15
@Author  : Sunflower
@FileName: BA.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res ^= num     #任何数跟0异或均为它本身，数组中除那一个数外，其他数均异或到最后为0。
        return res