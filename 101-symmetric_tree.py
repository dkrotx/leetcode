# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return not root or self.checkEqualLR(root.left, root.right)
    
    def checkEqualLR(self, lnode, rnode):
        if lnode == rnode == None:
            return True
        
        return bool(lnode and rnode) and lnode.val == rnode.val and \
               self.checkEqualLR(lnode.left, rnode.right) and \
               self.checkEqualLR(lnode.right, rnode.left)
