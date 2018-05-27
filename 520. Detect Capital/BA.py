# -*- coding: utf-8 -*-
"""
@Time    : 2018/2/12 14:38
@Author  : Sunflower
@FileName: BA.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""

class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.isupper() or word.islower() or word.istitle() #istitle()判断是否首字母为大写，其他均为小写