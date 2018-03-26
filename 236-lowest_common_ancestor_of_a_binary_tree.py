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
        self.lowestAncestor = None
        self.lookupNodes(root, p, q)
        return self.lowestAncestor
    
    def lookupNodes(self, node, p, q):
        nfound = 0
        if node:
            if node is p or node is q:
                nfound = 1

            for n in node.left, node.right:
                nfound += self.lookupNodes(n, p, q)
                
            if nfound == 2 and not self.lowestAncestor:
                self.lowestAncestor = node
            
        return nfound
