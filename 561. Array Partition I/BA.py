# -*- coding: utf-8 -*-
"""
@Time    : 2018/1/18 21:17
@Author  : Sunflower
@FileName: BA.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""


class Solution(object):

    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])   #sorted(nums)[::2]返回排序后的nums数组，且不是返回所有，而是间隔一位返回