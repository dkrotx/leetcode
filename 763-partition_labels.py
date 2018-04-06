class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        partitions = []
        max_poses = dict()
        for pos, c in enumerate(S):
            max_poses[c] = pos
        
        begin = border = 0
        for pos, c in enumerate(S):
            border = max(border, max_poses[c])
            if pos == border:
                partitions.append(pos - begin + 1)
                begin = border = pos + 1
                
        return partitions
