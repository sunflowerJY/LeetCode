# -*- coding: utf-8 -*-
"""
@Time    : 2018/2/3 17:36
@Author  : Sunflower
@FileName: 693. Binary Number with Alternating Bits.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""
"""

Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different
values.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101

Example 2:
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.

Example 3:
Input: 11
Output: False
Explanation:
The binary representation of 11 is: 1011.

Example 4:
Input: 10
Output: True
Explanation:
The binary representation of 10 is: 1010.
"""


class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if len(list(bin(n))) > 3:
            tmp = list(bin(n))[2]
            flag = 0
            for i in range(3, len(list(bin(n)))):
                if tmp == '1':     #翻转，例如：tmp为1，则re_tmp为0；
                    re_tmp = '0'
                else:
                    re_tmp = '1'
                if list(bin(n))[i] == re_tmp:
                    flag += 1
                    tmp = re_tmp
            if flag == len(list(bin(n))) - 3:
                return True
            else:
                return False
        else:
            return True





a = Solution()
print(a.hasAlternatingBits(1))