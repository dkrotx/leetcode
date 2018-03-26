# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        self.levels_info = []
        self.traverseAndCount(root, 0)
        
        ret = []
        for inf in self.levels_info:
            ret.append(float(inf[0]) / inf[1])
            
        return ret
        
    def traverseAndCount(self, node, depth):
        if not node:
            return
        
        assert(depth <= len(self.levels_info))
        if depth == len(self.levels_info):
            self.levels_info.append([0, 0]) # {sum, n}
        
        self.levels_info[depth][0] += node.val
        self.levels_info[depth][1] += 1
        
        for n in node.left, node.right:
            self.traverseAndCount(n, depth + 1)
