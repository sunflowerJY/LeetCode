# -*- coding: utf-8 -*-
"""
@Time    : 2018/2/7 8:21
@Author  : Sunflower
@FileName: 485. Max Consecutive Ones.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_0 = nums.count(0)
        if not count_0:
            return len(nums)
        else:
            len_nums = len(nums)
            arr = []
            for i in range(count_0):
                position_0 = nums.index(0)
                arr.append(position_0)
                nums = nums[position_0 + 1:]
            last_position_0 = len_nums - sum(arr) - count_0
            return max(arr) if max(arr) >= last_position_0 else last_position_0


S = Solution()
print(S.findMaxConsecutiveOnes([1]))


