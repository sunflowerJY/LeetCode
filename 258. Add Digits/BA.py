# -*- coding: utf-8 -*-
"""
@Time    : 2018/2/12 18:02
@Author  : Sunflower
@FileName: BA.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""

class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            num = sum(int(item) for item in str(num))
        return num


S = Solution()
print(S.addDigits(num=38))