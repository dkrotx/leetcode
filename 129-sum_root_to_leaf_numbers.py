# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return Solution._sum_leaves(root, 0)
        
    @staticmethod
    def _sum_leaves(node, num):
        num = num * 10 + node.val
        
        if not node.left and not node.right:
            return num
        
        total = 0
        if node.left:
            total += Solution._sum_leaves(node.left, num)
        if node.right:
            total += Solution._sum_leaves(node.right, num)
        
        return total
