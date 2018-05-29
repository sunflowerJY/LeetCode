# -*- coding: utf-8 -*-
"""
@Time    : 2018/5/28 16:37
@Author  : Sunflower
@FileName: version-1.py
@Software: PyCharm
@Blog    ：https://sunflowerjy.github.io
"""
"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的
三元组。
注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

from itertools import combinations


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        over = []
        for item in list(combinations(nums, 3)):
            if sum(item) == 0:
                res.append(list(item))

        for i in range(len(res) - 1):
            for j in range(i+1, len(res)):
                if sorted(res[i]) == sorted(res[j]):
                    over.append(j)

        for item in sorted(set(over), reverse=True):
            del res[item]
        return res



a = Solution()
print(a.threeSum(nums=[-1, 0, 1, 2, -1, -4]))
