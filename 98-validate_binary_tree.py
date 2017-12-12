# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return Solution.is_valid_subtree(root, None, None)
    
    @staticmethod
    def is_valid_subtree(node, min_val, max_val):
        if not node:
            return True
            
        if min_val is not None and node.val <= min_val:
            return False
        if max_val is not None and node.val >= max_val:
            return False
        
        valid_left = Solution.is_valid_subtree(node.left, min_val, node.val)
        valid_right = Solution.is_valid_subtree(node.right, node.val, max_val)
        
        return valid_left and valid_right
