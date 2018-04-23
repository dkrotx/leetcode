# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.pruneSubtree(root)
        
    def pruneSubtree(self, node):
        if not node:
            return None
        
        node.left = self.pruneSubtree(node.left)
        node.right = self.pruneSubtree(node.right)
        
        if not node.left and not node.right:
            return node if node.val == 1 else None
        
        return node
