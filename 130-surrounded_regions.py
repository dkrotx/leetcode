class Solution:
    def perimeter(self):
        for col in range(self.ncols):
            yield 0, col
            yield self.nrows - 1, col

        for row in range(self.nrows):
            yield row, 0
            yield row, self.ncols - 1
                
    def markRegionPassed(self, r, c):
        self.board[r][c] = 'P'
        stk = [(r, c)]

        while stk:
            r, c = stk.pop()
            for rn, cn in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= rn < self.nrows and 0 <= cn < self.ncols and self.board[rn][cn] == 'O':
                    self.board[rn][cn] = 'P'
                    stk.append((rn, cn))
        
            
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not any(board): return
        
        self.board = board
        self.nrows = len(board)
        self.ncols = len(board[0])
        
        """
        look for 'O' in perimeter: if found, fill region with 'P' (passed)
        """
        for row, col in self.perimeter():
            if board[row][col] == 'O':
                self.markRegionPassed(row, col)
                
        """
        Mark all 'P' regions by 'O' since they are opened
        And regions with 'O' are surrounded, mark 'em 'X'
        """
        for row in board:
            for i, v in enumerate(row):
                row[i] = 'XO'[v == 'P']
