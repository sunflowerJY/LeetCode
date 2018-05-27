# -*- coding: utf-8 -*-
"""
@Time    : 2018/2/5 20:40
@Author  : Sunflower
@FileName: BA1.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)  #聪明啊！
