"""
The best answer is to use the function-counter(),which can count the sub-string in the string
"""

class Solution:
    def judgeCircle(self, moves):
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')


a = Solution()
x = "UDD"
print(a.judgeCircle(moves=x))