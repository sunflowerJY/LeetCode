# -*- coding: utf-8 -*-
"""
@Time    : 2018/1/19 21:00
@Author  : Sunflower
@FileName: 476. Number Complement.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""
"""
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary 
representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.

Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to 
output 2.

Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to 
output 0.
"""


class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        tmp = []
        tmp_trans = []
        a = bin(num)
        b = ''
        for i in range(len(a)):
            tmp.append(a[i]) #tmp:将转换成二进制的字符串存到数组里
        for i in range(len(tmp)):
            if not(i == 0 or i == 1):
                if tmp[i] == '1':
                    tmp_trans.append('0')
                else:tmp_trans.append('1')   # tmp_trans:将原始二进制数组里‘1’‘0’互换
        for i in range(len(tmp_trans)):
            b = b + tmp_trans[i]
        return int(b, 2)


x = Solution()
print(x.findComplement(num=1))

