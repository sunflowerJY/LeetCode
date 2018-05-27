# -*- coding: utf-8 -*-
"""
@Time    : 2018/2/5 17:05
@Author  : Sunflower
@FileName: 136. Single Number.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""
"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_g = sorted(nums)
        for i in range(len(nums_g)-1):
            if i % 2 == 0:
                if nums_g[i] != nums_g[i + 1]:
                    return nums_g[i]
        return nums_g[-1]


a = Solution()
print(a.singleNumber(nums=[1, 10, 1, 2, 2, 10, 5]))

