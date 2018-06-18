# -*- coding: utf-8 -*-
"""
@Time    : 2018/6/17 19:49
@Author  : Sunflower
@FileName: 18. 四数之和.py
@Software: PyCharm
@Blog    ：https://sunflowerjy.github.io
"""

"""
给定一个包含n个整数的数组nums和一个目标值target,判断nums中是否存在四个元素 a，b，c 和 d ，
使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：
答案中不可以包含重复的四元组。

示例：
给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res_set = []
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                for k in range(j+1, len(nums)-1):
                    res = target - (nums[i] + nums[j] +nums[k])
                    buff_list = [nums[i], nums[j], nums[k]]
                    for m in range(k+1, len(nums)):
                        if nums[m] == res:
                            buff_list.append(nums[m])
                            res_set.append(buff_list)
                            break
        result = []
        [result.append(i) for i in res_set if i not in result]
        return result


a = Solution()
print(a.fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))



