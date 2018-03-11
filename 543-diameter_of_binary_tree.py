# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.found_max = 0
        self.calcDiameter(root)
        return self.found_max
        
    def calcDiameter(self, node):
        if not node:
            return 0
        
        lpath = self.calcDiameter(node.left)
        rpath = self.calcDiameter(node.right)
        sub_d = lpath + rpath
        self.found_max = max(self.found_max, sub_d)
        return max(lpath, rpath) + 1
