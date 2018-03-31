# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.leaves = []
        self.recordDieOrder(root)
        return self.leaves
        
    def recordDieOrder(self, node):
        if not node:
            return -1
        
        order = max(self.recordDieOrder(node.left), self.recordDieOrder(node.right)) + 1
        if order == len(self.leaves):
            self.leaves.append([])
            
        self.leaves[order].append(node.val)
        return order
