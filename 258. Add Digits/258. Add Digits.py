# -*- coding: utf-8 -*-
"""
@Time    : 2018/2/12 14:45
@Author  : Sunflower
@FileName: 258. Add Digits.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""
"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""


def helper(num):
    string = str(num)
    res = 0
    for item in string:
        res += int(item)
    return res


class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while len(str(num)) != 1:
            num = helper(num)
        return num


S = Solution()
print(S.addDigits(num=38))
