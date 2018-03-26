# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.best = []
        self.best4Depth(root, 0)
        return self.best
        
    def best4Depth(self, node, depth):
        if not node:
            return
        
        if depth < len(self.best):
            self.best[depth] = max(node.val, self.best[depth])
        else:
            assert(depth == len(self.best)) # we moving down only by 1 step
            self.best.append(node.val)
            
        for node in node.left, node.right:
            self.best4Depth(node, depth+1)
