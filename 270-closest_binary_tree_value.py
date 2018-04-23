# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.target = target
        self.closest = None
        
        self.findClosest(root)
        return self.closest
    
    def findClosest(self, node):
        if not node:
            return
        
        diff = node.val - self.target
        if self.closest is None or abs(diff) < abs(self.target - self.closest):
            self.closest = node.val
            
        if diff > 0:
            self.findClosest(node.left)
        else:
            self.findClosest(node.right)
