# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict

class Solution:
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        columns = defaultdict(list)
        frontier = [(0, root)] # 0 is coordinate on X-axis
        x_min, x_max = 0, 0
        
        while frontier:
            next_frontier = []
            for x, node in frontier:
                columns[x].append(node.val)
                x_min = min(x_min, x)
                x_max = max(x_max, x)
                if node.left:
                    next_frontier.append((x - 1, node.left))
                if node.right:
                    next_frontier.append((x + 1, node.right))
                    
            frontier = next_frontier
                
        return [columns[x] for x in range(x_min, x_max + 1)]
