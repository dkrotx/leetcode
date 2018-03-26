# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.levels = []
        self.dumpPreorder(root, 0)
        return list(reversed(self.levels))
        
    def dumpPreorder(self, node, depth):
        if not node:
            return
        
        assert(depth <= len(self.levels)) # we are moving step-by-step down, not at random
        
        if depth == len(self.levels):
            self.levels.append([])    
        self.levels[depth].append(node.val)
        
        for n in node.left, node.right:
            self.dumpPreorder(n, depth+1)
