# -*- coding: utf-8 -*-
"""
@Time    : 2018/1/28 21:09
@Author  : Sunflower
@FileName: BA1.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""
#Solution 2 - Oneliner
class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        def matrixReshape(self, nums, r, c):
            flat = sum(nums, []) #将多维秒变一维数组
            if len(flat) != r * c:
                return nums
            tuples = zip(*([iter(flat)] * c))
            return map(list, tuples)