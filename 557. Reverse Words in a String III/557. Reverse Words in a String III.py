# -*- coding: utf-8 -*-
"""
@Time    : 2018/1/20 15:17
@Author  : Sunflower
@FileName: 557. Reverse Words in a String III.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""
"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""


class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmp = ''
        re_tmp = ''
        for i in range(len(s)):
            if s[i] != ' ':
                tmp += s[i]
            if s[i] == ' ':
                re_tmp = re_tmp + tmp[::-1] + ' ' #倒序
                tmp = ''  #清空，只存储一个单词
            if i == len(s) - 1:
                re_tmp = re_tmp + tmp[::-1]  # 倒序

        return re_tmp


a = Solution()
print(a.reverseWords(s="Let's take LeetCode contest"))

