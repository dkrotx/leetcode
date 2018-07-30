# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def collectLeafs(node, leafs):
            if not node:
                return leafs
            if not node.left and not node.right:
                leafs.append(node.val)
            else:
                collectLeafs(node.left, leafs)
                collectLeafs(node.right, leafs)
                
            return leafs
        
        return collectLeafs(root1, []) == collectLeafs(root2, [])
