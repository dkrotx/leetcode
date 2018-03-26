# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        frontier = [root]
        
        while any(frontier):
            next_frontier, cur_level = [], []
            for node in frontier:
                cur_level.append(node.val)
                next_frontier.extend(list(filter(None, [node.left, node.right])))
            
            levels.append(cur_level)
            frontier = next_frontier
            
        return levels
