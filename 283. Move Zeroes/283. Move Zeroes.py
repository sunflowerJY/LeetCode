# -*- coding: utf-8 -*-
"""
@Time    : 2018/2/11 8:23
@Author  : Sunflower
@FileName: 695. Max Area of Island.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""
"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the 
non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count_0 = nums.count(0)
        while 0 in nums:
            nums.remove(0)
        for i in range(count_0):
            nums.append(0)

S = Solution()
nums=[0,1,0,3,12]
S.moveZeroes(nums)
print(nums)