# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        node = root
        stk, prev = [], None
        while node or stk:
            while node:
                stk.append(node)
                if prev:
                    prev.left = node
                prev = node
                node = node.left
                
            if stk:
                node = stk.pop().right
                
        """ now all nodes flattened by left pointer
            we have to switch it to right
        """
        node = root
        while node:
            next_node = node.left
            node.left, node.right = None, node.left
            node = next_node
