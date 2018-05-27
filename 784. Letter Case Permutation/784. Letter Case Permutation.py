# -*- coding: utf-8 -*-
"""
@Time    : 2018/2/18 20:56
@Author  : Sunflower
@FileName: 784. Letter Case Permutation.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""
"""
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  
Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]

Note:

S will be a string with length at most 12.
S will consist only of letters or digits.
"""
from itertools import product

class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        L = [[i.lower(), i.upper()] if i.isalpha() else i for i in S]
        return [''.join(i) for i in product(*L)]



X = Solution()
print(X.letterCasePermutation(S="a1b2"))
