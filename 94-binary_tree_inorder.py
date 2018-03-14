# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node = root
        res, stk = [], []
        
        while node or stk:
            while node:
                stk.append(node)
                node = node.left

            while not node and stk:
                node = stk.pop()
                res.append(node.val)
                node = node.right
        
        return res
