# -*- coding: utf-8 -*-
"""
@Time    : 2018/2/4 12:34
@Author  : Sunflower
@FileName: 292. Nim Game.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""
"""
You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you 
take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn 
to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win 
the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2,or 3 stones you remove,
 the last stone will always be removed by your friend.
"""


class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return False if not n % 4 else True


a = Solution()
print(a.canWinNim(n=1))