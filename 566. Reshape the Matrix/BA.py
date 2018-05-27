# -*- coding: utf-8 -*-
"""
@Time    : 2018/1/28 21:02
@Author  : Sunflower
@FileName: BA.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""
import numpy as np

#Solution 1 - NumPy
class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        def matrixReshape(self, nums, r, c):
            try:
                return np.reshape(nums, (r, c)).tolist()
            except:
                return nums