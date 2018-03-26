# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.view = []
        # since we moving pre-order, right value will be filled last
        self.fillView4Level(root, 0)
        return self.view
        
    def fillView4Level(self, node, depth):
        if not node:
            return
        
        if depth < len(self.view):
            self.view[depth] = node.val
        else:
            assert(depth == len(self.view))
            self.view.append(node.val)
        
        for n in node.left, node.right:
            self.fillView4Level(n, depth+1)
