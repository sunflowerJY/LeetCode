"""
657. Judge Route Circle
Created on 2018/1/13
@author:Sunflower
"""
"""
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, 
which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are 
R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a 
circle.

Example 1:
Input: "UD"
Output: true

Example 2:
Input: "LL"
Output: false
"""

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        l = r = u = d = 0

        if len(moves) % 2 == 0:  #字符个数为偶数，可能是循环，也可能不是循环
            for i in range(len(moves)):
                if moves[i] == "L":
                    l += 1
                if moves[i] == "R":
                    r += 1
                if moves[i] == "U":
                    u += 1
                if moves[i] == "D":
                    d += 1
            if l == r and u == d:   ##痛点
                return True
            else:
                return False
        else:
            return False

a = "UD"
x = Solution()
print(x.judgeCircle(moves=a))

"""
痛点解析：
& 和 and的区别：
    &:位运算符  处理对象：二进制 按位与
    and:逻辑运算符  处理对象：布尔值
"""




