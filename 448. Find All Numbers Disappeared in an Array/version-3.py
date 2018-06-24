# -*- coding: utf-8 -*-
"""
@Time    : 2018/6/19 22:08
@Author  : Sunflower
@FileName: version-3.py
@Software: PyCharm
@Blog    ：https://sunflowerjy.github.io
"""
"""
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
找到所有在 [1, n] 范围之间没有出现在数组中的数字。
您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:
输入:
[4,3,2,7,8,2,3,1]
输出:
[5,6]
"""

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        new = list(set(nums))
        for i in range(len(new) - 1):
            distance = new[i + 1] - new[i]
            if distance != 1:
                for j in range(1, distance):
                    res.append(new[i] + j)
        return res

a = Solution()
print(a.findDisappearedNumbers(nums=[1, 1]))