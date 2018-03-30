# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.findLCA(root, p.val, q.val)
        
    def findLCA(self, node, a, b):
        if a < node.val and b < node.val:
            return self.findLCA(node.left, a, b)
            
        if a > node.val and b > node.val:
            return self.findLCA(node.right, a, b)
        
        """ first node from which comes different directions of 'a' and 'b' is LCA """
        return node
