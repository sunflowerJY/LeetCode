# -*- coding: utf-8 -*-
"""
@Time    : 2018/1/20 17:20
@Author  : Sunflower
@FileName: BA.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""


class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        def reverseWords(self, s):
            return ' '.join(x[::-1] for x in s.split())


a = Solution()
print(a.reverseWords(s="Let's take LeetCode contest"))