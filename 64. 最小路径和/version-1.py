# -*- coding: utf-8 -*-
"""
@Time    : 2018/6/23 17:46
@Author  : Sunflower
@FileName: version-1.py
@Software: PyCharm
@Blog    ：https://sunflowerjy.github.io
"""
"""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
"""


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = grid[0][0]
        i = 0
        j = 0
        if len(grid) == 1 and len(grid[0]) != 1:
            for m in range(len(grid[0])):
                res += grid[0][m]
        if len(grid[0]) == 1 and len(grid) != 1:
            for n in range(len(grid)):
                res += grid[n][0]
        if len(grid) == 1 and len(grid[0]) == 1:
            res += grid[0][0]
        while i < len(grid) and j < len(grid[0]):
            if i == len(grid)-1:
                j += 1
                while j < len(grid[0]):
                    res += grid[i][j]
                    j += 1
                break
            if j == len(grid[0])-1:
                i += 1
                while i < len(grid):
                    res += grid[i][j]
                    i += 1
                break
            if grid[i][j+1] <= grid[i+1][j]:
                res += grid[i][j+1]
                j += 1
            else:
                res += grid[i+1][j]
                i += 1
        return res


a = Solution()
print(a.minPathSum(grid=[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))