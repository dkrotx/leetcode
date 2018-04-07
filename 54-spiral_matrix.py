class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not any(matrix):
            return []
        
        height, width = len(matrix), len(matrix[0])
        row, col = 0, 0
        d = 0
        res = []
        
        while True:
            if col >= width - d:
                break
            while col < width - d:
                res.append(matrix[row][col])
                col += 1
            
            row += 1; col = width - 1 - d
            if row >= height - d:
                break
            while row < height - d:
                res.append(matrix[row][col])
                row += 1
                
            col -= 1; row = height - 1 - d
            if col < d:
                break
            while col >= d:
                res.append(matrix[row][col])
                col -= 1
            
            row -= 1; col = d
            if row <= d:
                break
            while row > d:
                res.append(matrix[row][col])
                row -= 1
            
            # moving to next loop
            d += 1
            row = d; col += 1
            
                
        return res
