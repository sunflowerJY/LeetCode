# -*- coding: utf-8 -*-
"""
@Time    : 2018/5/29 16:13
@Author  : Sunflower
@FileName: version-1.py
@Software: PyCharm
@Blog    ：https://sunflowerjy.github.io
"""
"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，
使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
"""


from itertools import combinations

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res_sum = []
        res_abs = []
        for item in combinations(nums, 3):
            res_sum.append(sum(item))
        for nums_sum in res_sum:
            res_abs.append(abs(target - nums_sum))
        for index, val in enumerate(res_abs):
            if val == min(res_abs):
                return res_sum[index]

a = Solution()
print(a.threeSumClosest(nums=[-1, 2, 1, -4], target=1))
