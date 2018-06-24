# -*- coding: utf-8 -*-
"""
@Time    : 2018/6/22 10:30
@Author  : Sunflower
@FileName: version-1.py
@Software: PyCharm
@Blog    ：https://sunflowerjy.github.io
"""
"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。
请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。

示例 1:
nums1 = [1, 3]
nums2 = [2]
中位数是 2.0

示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
中位数是 (2 + 3)/2 = 2.5
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        res = nums1 + nums2
        res.sort()
        if len(res) % 2 == 0:
            return (res[int(len(res)/2)-1]+res[int(len(res)/2)])/2
        else:
            return res[int((len(res)-1)/2)]


a = Solution()
print(a.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))