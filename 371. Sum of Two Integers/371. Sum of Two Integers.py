# -*- coding: utf-8 -*-
"""
@Time    : 2018/2/17 22:53
@Author  : Sunflower
@FileName: 371. Sum of Two Integers.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""
"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
"""


class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        tmp = list()
        tmp.append(a)
        tmp.append(b)
        return sum(tmp)


S = Solution()
print(S.getSum(a=1, b=2))