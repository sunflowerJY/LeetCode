# -*- coding: utf-8 -*-
"""
@Time    : 2018/2/14 9:29
@Author  : Sunflower
@FileName: 448. Find All Numbers Disappeared in an Array.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""
"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]
Output:
[5,6]
"""


class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            if i+1 not in nums:
                res.append(i + 1)
        return res


S = Solution()
print(S.findDisappearedNumbers(nums=[1, 1]))