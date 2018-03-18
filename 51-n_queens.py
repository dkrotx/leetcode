class Solution:
    ints2ext = ['.', 'Q', '.']
    
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.size = n
        self.solutions = []
        """
        table cells meaning:
         - 0: free
         - 1: queen
         - 2*q: attacked by q queens
        """
        self.table = [ [0 for _ in range(n)] for _ in range(n) ]
        
        self.placeQueenInRow(0)
        return self.solutions
        
    def markLine(self, add_val, row, col, delta_row, delta_col):
        while 0 <= row < self.size and 0 <= col < self.size:
            self.table[row][col] += add_val
            row += delta_row
            col += delta_col
        
    def markRegion(self, row, col, mark1, mark2):
        self.markLine(mark2, row, 0, 0, 1) # horizontal
        self.markLine(mark2, 0, col, 1, 0) # vertical
        self.markLine(mark2, row, col, -1, -1) # left-up
        self.markLine(mark2, row, col, +1, -1) # left-down
        self.markLine(mark2, row, col, -1, +1) # right-up
        self.markLine(mark2, row, col, +1, +1) # right-down
        
        self.table[row][col] = mark1 # mark self
        
    def markQueenPlacement(self, row, col):
        self.markRegion(row, col, 1, +2)
        
    def unmarkQueenPlacement(self, row, col):
        self.markRegion(row, col, 0, -2)
        
    def table2Solution(self):
        res = []
        
        for row in range(self.size):
            final_row = []
            for col in range(self.size):
                val = self.table[row][col]
                final_row.append('Q' if val == 1 else '.')
            res.append(''.join(final_row))
            
        return res
        
    def placeQueenInRow(self, row):
        if row == self.size:
            self.solutions.append(self.table2Solution())
            return

        for col in range(self.size):
            if not self.table[row][col]:
                self.markQueenPlacement(row, col)
                self.placeQueenInRow(row+1)
                self.unmarkQueenPlacement(row, col)
