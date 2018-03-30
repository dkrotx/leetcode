# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.findLongestCons(root)
        
    def findLongestCons(self, node, prev=None, cur_len=0):
        if not node:
            return cur_len
        
        if prev is not None and node.val != prev+1:
            cur_len = 0
        cur_len += 1
        
        return max(
            self.findLongestCons(node.left, node.val, cur_len),
            self.findLongestCons(node.right, node.val, cur_len),
            cur_len
        )
