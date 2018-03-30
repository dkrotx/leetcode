# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.paths = []
        self.ensurePathSum(root, sum, [])
        return self.paths
        
    def ensurePathSum(self, node, rest, path):
        if not node:
            return
        
        path.append(node.val)
        if not node.left and not node.right:
            if rest == node.val:
                self.paths.append(path[:])
        else:
            for n in filter(None, [node.left, node.right]):
                self.ensurePathSum(n, rest - node.val, path)
            
        path.pop() # speedup by not copying array
