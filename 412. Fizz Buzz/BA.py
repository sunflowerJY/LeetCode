# -*- coding: utf-8 -*-
"""
@Time    : 2018/1/27 14:00
@Author  : Sunflower
@FileName: test.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""

class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def fizzBuzz(self, n):
            return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n + 1)]