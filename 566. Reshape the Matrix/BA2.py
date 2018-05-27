# -*- coding: utf-8 -*-
"""
@Time    : 2018/1/28 21:49
@Author  : Sunflower
@FileName: BA2.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""
import itertools


class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        def matrixReshape(self, nums, r, c):
            if r * c != len(nums) * len(nums[0]):
                return nums
            it = itertools.chain(*nums)
            return [list(itertools.islice(it, c)) for _ in xrange(r)]

nums = [[1, 2], [3, 4]]
a = Solution()
print(a.matrixReshape(nums=nums, r=1, c=4))