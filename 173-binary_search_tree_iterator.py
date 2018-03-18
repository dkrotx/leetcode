# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Do in-order iteration using stack
"""
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.node = root
        self.stk = []
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.node or self.stk
        

    def next(self):
        """
        :rtype: int
        """
        while self.node:
            self.stk.append(self.node)
            self.node = self.node.left
        
        if not self.stk:
            raise StopIteration("no more items in BSTIterator")
        
        popped = self.stk.pop()
        self.node = popped.right
        return popped.val
        
# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
