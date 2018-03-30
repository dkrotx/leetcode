# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, node):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stk = []
        
        while node or stk:
            while node:
                stk.append([node, 2]) # 2 is the number of paths left to visit from the node
                node = node.left
            
            if stk:
                stk[-1][1] -= 1
                if stk[-1][1] == 0:
                    res.append(stk.pop()[0].val)
                else:
                    node = stk[-1][0].right
                    
        return res
