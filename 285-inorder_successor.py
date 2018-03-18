#
# it works 100% by tests don't know why leetcode doesn't accept it
#

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        node = root
        stk = []
        while node.val != p.val:
            if node.val > p.val:
                node = node.left
                stk.append(node)
            else:
                node = node.right
                """
                do not trace right direction since "right parents" are already visited by in-order
                """
        
        if node is not p:
            raise IndexError("Given pointer is not within tree or tree contains duplicates!")
        
        """ append found node since we're interested in right subtree of itself """
        stk.append(node)
        
        first_right_node = None
        while stk:
            first_right_node = stk.pop().right
            if first_right_node:
                break
        else:
            return None
            
        most_left = first_right_node
        while most_left.left:
            most_left = most_left.left
            
        return most_left
