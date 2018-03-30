# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def concatWithoutDuplicates(self, root, left, leaves, right):
        res = left[:]
        skip_leaves = 1 if root.left or (not root.left and not root.right) else 0
        
        for e in leaves[skip_leaves:]:
            res.append(e)
            
        for e in right[1:-1]:
            res.append(e)

        return res
        
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        lbound = self.leftBoundary(root, []) if root.left else [root.val]
        rbound = list(reversed(self.rightBoundary(root, []))) if root.right else [root.val]
        leaves = self.getLeaves(root, [])
        
        return self.concatWithoutDuplicates(root, lbound, leaves, rbound)
        
    def leftBoundary(self, node, path):
        path.append(node.val)
        for n in filter(None, [node.left, node.right]):
            self.leftBoundary(n, path)
            break
            
        return path
    
    def rightBoundary(self, node, path):
        path.append(node.val)
        for n in filter(None, [node.right, node.left]):
            self.rightBoundary(n, path)
            break
            
        return path
    
    def getLeaves(self, node, leaves):
        if not node.left and not node.right:
            leaves.append(node.val)
        else:
            for n in filter(None, [node.left, node.right]):
                self.getLeaves(n, leaves)
                
        return leaves
