# -*- coding: utf-8 -*-
"""
@Time    : 2018/5/27 20:08
@Author  : Sunflower
@FileName: version-1.py
@Software: PyCharm
@Blog    ：https://sunflowerjy.github.io
"""
"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
画 n 条垂直线，使得垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，
使得它们与 x 轴共同构成的容器可以容纳最多的水。

注意：你不能倾斜容器，n至少是2。
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        max{(i-j)*min(ai,aj)} if i>j
        """
        n = len(height)
        l, r = 0, n-1
        max_area = min(height[l], height[r])*(r-l)
        while r > l:
            if height[r] >= height[l]:
                l += 1
            elif height[r] < height[l]:
                r -= 1
            max_area = max(max_area, min(height[l], height[r])*(r-l))
        return max_area

a = Solution()
print(a.maxArea(height=[2, 3.5, 2.8, 1]))