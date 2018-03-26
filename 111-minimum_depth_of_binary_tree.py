# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.getMinDepth(root, 1) if root else 0
        
    def getMinDepth(self, node, d):
        if not node.left and not node.right:
            return d
        
        if node.left and node.right:
            return min(self.getMinDepth(node.left, d+1), self.getMinDepth(node.right, d+1))
        
        return self.getMinDepth(node.left or node.right, d+1)
