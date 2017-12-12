# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        def depth(node):
            if node is None:
                return 0
            return max(depth(node.left), depth(node.right))+1
            
        return depth(root)
