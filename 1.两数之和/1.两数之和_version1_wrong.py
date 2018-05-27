# -*- coding: utf-8 -*-
"""
@Time    : 2018/5/6 22:39
@Author  : Sunflower
@FileName: 1.两数之和.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""

"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""

from itertools import combinations

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        for team in list(combinations(nums, r=2)):
            x, y = team
            if x + y == target:
                res.append(nums.index(x))
                res.append(nums.index(y))
                return res

#出错！

nums = [3,3]
target = 6
a = Solution()
print(a.twoSum(nums = nums, target = target))
