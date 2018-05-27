# -*- coding: utf-8 -*-
"""
@Time    : 2018/2/1 17:26
@Author  : Sunflower
@FileName: 496. Next Greater Element I.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""
"""
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the 
next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, 
output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
    
Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
"""


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for item1 in nums1:
            flag = 0
            if nums2.index(item1)+1 == len(nums2):
                res.append(-1)
            else:
                for i in range(nums2.index(item1) + 1, len(nums2)):
                    if nums2[i] > item1:
                        res.append(nums2[i])
                        flag = 1
                        break
                if not flag:
                    res.append(-1)
        return res


a = Solution()
print(a.nextGreaterElement(nums1=[2,4], nums2=[1,2,3,4]))