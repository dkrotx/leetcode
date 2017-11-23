class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        """ 
        idea:
            - look at each element
            - if it's 0, then mark this row or column as zero
              (setting value in column #0 and row #0 to 0)
            - handle row #0 and column #0 itself in special way
            - second step: look for row #0, column #0 and values of reset_r0, reset_c0
              to zero appropriate cells or rows
              
        Time-compexity is O(m*n), space complexity is O(1)
        """
        
        def zero_row(r):
            for c in range(len(matrix[r])):
                matrix[r][c] = 0

        def zero_column(c):
            for r in range(len(matrix)):
                matrix[r][c] = 0
        
        reset_r0, reset_c0 = False, False
        
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    if r and c:
                        matrix[r][0] = 0
                        matrix[0][c] = 0
                    else:
                        if r == 0:
                            reset_r0 = True
                        if c == 0:
                            reset_c0 = True
                        
                        
        for c in range(1, len(matrix[0])):
            if not matrix[0][c]:
                zero_column(c)
                
        for r in range(1, len(matrix)):
            if not matrix[r][0]:
                zero_row(r)
                
        if reset_c0:
            zero_column(0)
        if reset_r0:
            zero_row(0)
