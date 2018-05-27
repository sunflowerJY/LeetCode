# -*- coding: utf-8 -*-
"""
@Time    : 2018/1/20 14:31
@Author  : Sunflower
@FileName: BA.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""


class Solution(object):
    def findComplement(self, num):
        i = 1
        while i <= num:
            i = i << 1
        return (i - 1) ^ num


x = Solution()
print(x.findComplement(num=5))