# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return False
        
        if s.val == t.val and self.cmpTrees(s, t):
            return True
            
        for child in filter(None, [s.left, s.right]):
            if self.isSubtree(child, t):
                return True
            
        return False
    
    def cmpTrees(self, a, b):
        return (not a and not b) or (a and b and a.val == b.val and \
                                   self.cmpTrees(a.left, b.left) and \
                                   self.cmpTrees(a.right, b.right))
