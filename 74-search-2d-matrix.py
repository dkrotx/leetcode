class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        l, u = 0, len(matrix)
        while l < u:
            m = (l + u) // 2
            if target > matrix[m][len(matrix[m])-1]:
                l = m+1
            else:
                u = m
                
        row = l
        if row < len(matrix):
            l, u = 0, len(matrix[row])
            while l < u:
                m = (l + u) // 2
                if target == matrix[row][m]:
                    return True

                if target > matrix[row][m]:
                    l = m+1
                else:
                    u = m
                
        return False
