# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.paths = []
        self.makePaths(root, [])
        return ['->'.join(map(str, x)) for x in self.paths]
        
    def makePaths(self, node, path):
        if not node:
            return
        
        path.append(node.val)
        
        if not node.left and not node.right:
            self.paths.append(path)
            return
            
        for n in filter(None, [node.left, node.right]):
            self.makePaths(n, path[:])
