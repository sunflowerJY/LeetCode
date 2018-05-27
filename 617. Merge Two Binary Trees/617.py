# -*- coding: utf-8 -*-
"""
@Time    : 2018/1/16 19:21
@Author  : Sunflower
@FileName: 617. Merge Two Binary Trees.py
@Software: PyCharm
@Blog    ：http://blog.csdn.net/sunflower_kris/article/
"""

"""
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are 
overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as 
the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:
Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
Note: The merging process must start from the root nodes of both trees.
"""
import showBT

null = None
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2: return None
        ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        return ans


S = Solution()
t1 = showBT.constructBinaryTree([1,3,2,5])
t2 = showBT.constructBinaryTree([2,1,3,null,4,null,7])
ans_tree = S.mergeTrees(t1, t2)
tree = showBT.outputBinaryTreeByDot(ans_tree)
showBT.showDotFile(tree)

#调试时，将本文件复制到C:\Users\sunfl下，并改名为617.py
#保证617.py和showBT.py在一个目录下，在cmd中，输入python 617.py