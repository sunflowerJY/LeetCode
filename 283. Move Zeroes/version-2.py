# -*- coding: utf-8 -*-
"""
@Time    : 2018/6/22 15:26
@Author  : Sunflower
@FileName: version-2.py
@Software: PyCharm
@Blog    ：https://sunflowerjy.github.io
"""
"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num_0 = nums.count(0)
        i = 0
        flag = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                flag += 1
                if flag == num_0:
                    break
            else:
                i += 1
        return nums


a = Solution()
print(a.moveZeroes(nums=[0,1,0,3,12]))
