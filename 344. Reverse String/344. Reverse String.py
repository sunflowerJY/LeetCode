# -*- coding: utf-8 -*-
"""
@Time    : 2018/1/21 10:20
@Author  : Sunflower
@FileName: 344. Reverse String.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""
"""
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
"""


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

a = Solution()
print(a.reverseString(s="hello"))