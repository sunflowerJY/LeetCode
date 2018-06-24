# -*- coding: utf-8 -*-
"""
@Time    : 2018/6/23 21:08
@Author  : Sunflower
@FileName: BA.py
@Software: PyCharm
@Blog    ：https://sunflowerjy.github.io
"""


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]


a = Solution()
print(a.minPathSum(grid=[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))