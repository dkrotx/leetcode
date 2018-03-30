# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, node):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stk = []
        
        while node or stk:
            if not node:
                node = stk.pop().right
                
            while node:
                res.append(node.val)
                stk.append(node)
                node = node.left
                
        return res
