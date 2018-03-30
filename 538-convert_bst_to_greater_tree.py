# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.modifyGreaterTree(root, 0)
        return root
        
    def modifyGreaterTree(self, node, bigger_sum):
        if not node:
            return 0
        
        right_sum = self.modifyGreaterTree(node.right, bigger_sum)
        left_sum = self.modifyGreaterTree(node.left, bigger_sum + node.val + right_sum)
        original_val = node.val
        node.val += bigger_sum + right_sum
        return left_sum + original_val + right_sum
