# Definition for a binary tree node.
# class TreeNode():
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SubtreeInfo:
    def __init__(self, is_bst, nnodes, minval, maxval=None):
        self.is_bst = is_bst
        self.nnodes = nnodes
        self.minval = minval
        self.maxval = maxval or minval

class Solution():
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_bst_nodes = 0
        if root:
            self.checkByPreorder(root)
        return self.max_bst_nodes
        
    def checkByPreorder(self, node):
        left_info, right_info = None, None
        left_ok, right_ok = True, True
        nnodes = 1 # account itself
        
        if node.left:
            left_info = self.checkByPreorder(node.left)
            left_ok = left_info.is_bst and left_info.maxval < node.val
            nnodes += left_info.nnodes
            
        if node.right:
            right_info = self.checkByPreorder(node.right)
            right_ok = right_info.is_bst and right_info.minval > node.val
            nnodes += right_info.nnodes
            
        if left_ok and right_ok:
            self.max_bst_nodes = max(nnodes, self.max_bst_nodes)
            return SubtreeInfo(True, nnodes,
                               left_info.minval if left_info else node.val,
                               right_info.maxval if right_info else node.val)
        
        return SubtreeInfo(False, 0, 0, 0)
