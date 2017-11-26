# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        self.balanced = True
        self.checkBalanced(root, 0)
        return self.balanced
    
    def checkBalanced(self, node, depth):
        if not node:
            return depth-1
        
        ld = self.checkBalanced(node.left, depth+1)
        rd = self.checkBalanced(node.right, depth+1)
        
        min_depth = min(ld, rd)
        max_depth = max(ld, rd)
        if max_depth - min_depth > 1:
            self.balanced = False
        
        return max_depth
