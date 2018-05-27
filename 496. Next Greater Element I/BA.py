# -*- coding: utf-8 -*-
"""
@Time    : 2018/2/2 20:04
@Author  : Sunflower
@FileName: BA.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""

class Solution:
    def nextGreaterElement(self, findNums, nums):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        def helper(num):
            for tmp in nums[nums.index(num):]:
                if tmp > num:
                    return tmp
            return -1

        return map(helper, findNums)


a = Solution()
print(list(a.nextGreaterElement(findNums=[2,4], nums=[1,2,3,4])))