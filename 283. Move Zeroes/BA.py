# -*- coding: utf-8 -*-
"""
@Time    : 2018/2/13 18:08
@Author  : Sunflower
@FileName: BA.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort(key=lambda x: 1 if x == 0 else 0)


S = Solution()
nums=[0,1,0,3,12]
S.moveZeroes(nums)
print(nums)