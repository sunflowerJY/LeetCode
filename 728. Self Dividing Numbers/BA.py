# -*- coding: utf-8 -*-
"""
@Time    : 2018/1/18 17:44
@Author  : Sunflower
@FileName: BA2.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""

"""
学会使用递归
"""

class Solution(object):

    def selfDividingNumbers(self, left, right):
        """
                :type left: int
                :type right: int
                :rtype: List[int]
                """
        return [num for num in range(left, right + 1) if all((int(d) and not num % int(d)) for d in str(num))]

a = Solution()
print(a.selfDividingNumbers(left=1, right=22))