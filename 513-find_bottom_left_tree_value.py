# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def find_depth_leftmost(node, depth):
            left = find_depth_leftmost(node.left, depth+1) if node.left else None
            right = find_depth_leftmost(node.right, depth+1) if node.right else None
            
            if left and right:
                return right if right[0] > left[0] else left
            if left:
                return left
            if right:
                return right
                
            return depth, node.val # leaf node
        
        return find_depth_leftmost(root, 0)[1]
