# -*- coding: utf-8 -*-
"""
@Time    : 2018/6/23 15:52
@Author  : Sunflower
@FileName: BA.py
@Software: PyCharm
@Blog    ：https://sunflowerjy.github.io
"""
class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        iniArr = [0]
        if num > 0:
            while len(iniArr) < num + 1:
                iniArr.extend([x + 1 for x in iniArr])

        return iniArr[0:num + 1]


a = Solution()
print(a.countBits(num=5))