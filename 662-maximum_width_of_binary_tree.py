class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.level_stats = []
        self.countLevelWidths(root, level=0, coord=1)
        return max(map(lambda x: x[1] - x[0] + 1, self.level_stats))
        
    def countLevelWidths(self, node, level, coord):
        if not node:
            return
        
        assert(level <= len(self.level_stats))
        if level == len(self.level_stats):
            self.level_stats.append([coord, coord])
        else:
            self.level_stats[level][0] = min(self.level_stats[level][0], coord)
            self.level_stats[level][1] = max(self.level_stats[level][1], coord)
            
        self.countLevelWidths(node.left,  level+1, coord*2 - 1)
        self.countLevelWidths(node.right, level+1, coord*2)
