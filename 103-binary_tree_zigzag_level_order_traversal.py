# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        frontier = [root]
        inverse = False
        
        while any(frontier):
            lvl = []
            next_frontier = []
            for node in frontier:
                next_frontier.extend(list(filter(None, [node.left, node.right])))
                lvl.append(node.val)
                    
            levels.append(list(reversed(lvl)) if inverse else lvl)
            frontier = next_frontier
            inverse = not inverse
            
        return levels
