# -*- coding: utf-8 -*-
"""
@Time    : 2018/2/15 10:26
@Author  : Sunflower
@FileName: BA.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""


from functools import reduce
import operator


class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return chr(reduce(operator.xor, map(ord, s + t)))


S = Solution()
print(S.findTheDifference(s="a", t="aa"))