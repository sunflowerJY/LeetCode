# -*- coding: utf-8 -*-
"""
@Time    : 2018/1/22 18:02
@Author  : Sunflower
@FileName: 500. Keyboard Row.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""
"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American 
keyboard like the image below.

Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""


class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        row2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        row3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']

        r_list = []
        for i in range(len(words)):
            count_row1 = count_row2 = count_row3 = 0
            for j1 in range(len(row1)):
                count_row1 += words[i].lower().count(row1[j1])
            if count_row1 == len(words[i]):
                r_list.append(words[i])
                continue
            for j2 in range(len(row2)):
                count_row2 += words[i].lower().count(row2[j2])
            if count_row2 == len(words[i]):
                r_list.append(words[i])
                continue
            for j3 in range(len(row3)):
                count_row3 += words[i].lower().count(row3[j3])
            if count_row3 == len(words[i]):
                r_list.append(words[i])
                continue
        return r_list

a = Solution()
print(a.findWords(words=["Hello", "Alaska", "Dad", "Peace"]))