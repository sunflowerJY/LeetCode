# -*- coding: utf-8 -*-
"""
@Time    : 2018/1/18 13:40
@Author  : Sunflower
@FileName: 728. Self Dividing Numbers.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""
"""
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
Note:

The boundaries of each input argument are 1 <= left <= right <= 10000.
"""


class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        while 1 <= left <= right <= 10000:   # int() can be replaced by // (eg. 22//10=2 , int(22/10)=2, 22/10=2.2
            if 1 <= left <= 9:
                res.append(left)
            if 10 <= left <= 99:
                if int(left / 10) != 0 and left % 10 != 0 and left % (int(left / 10)) == 0 and left % (left % 10) == 0:
                    res.append(left)
            if 100 <= left <= 999:
                if int(left / 100) != 0 and int(left / 10) % 10 != 0 and left % 10 != 0 and left % int((left / 100)) == \
                        0 and left % (int(left / 10) % 10) == 0 and left % (left % 10) == 0:
                    res.append(left)
            if 1000 <= left <= 9999:
                if int(left / 1000) != 0 and int(left / 100) % 10 != 0 and int(left / 10) % 10 != 0 \
                        and left % 10 != 0 and left % (int(left / 1000)) == 0 and left % (int(left / 100) % 10) == 0\
                        and left % (int(left / 10) % 10) == 0 and left % (left % 10) == 0:
                    res.append(left)
            left += 1
        return res


a = Solution()
print(a.selfDividingNumbers(left=1, right=22))


