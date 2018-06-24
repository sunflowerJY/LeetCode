# -*- coding: utf-8 -*-
"""
@Time    : 2018/1/18 20:06
@Author  : Sunflower
@FileName: 561. Array Partition I.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""
"""
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2),
 ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].
"""


class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        nums.sort()
        for i in range(len(nums)):
            if not i % 2:
                res += nums[i]
        return res


a = Solution()
print(a.arrayPairSum(nums=[1, 1]))