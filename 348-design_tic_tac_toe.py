class TicTacToe:
    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.grid = [[0]*n for _ in range(n)]
        
    def checkGrid(self, row, col, rd, cd, expected):
        while 0 <= row < self.n and 0 <= col < self.n:
            if self.grid[row][col] != expected:
                return False
            row += rd
            col += cd
            
        return True

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.grid[row][col] = player
        
        # check horizontal and vertical
        if self.checkGrid(row, 0, 0, 1, player) or self.checkGrid(0, col, 1, 0, player):
            return player
        
        # check first diagonal
        if row == col and self.checkGrid(0, 0, 1, 1, player):
            return player
        
        # check second diagonal
        if row == self.n - col - 1 and self.checkGrid(self.n - 1, 0, -1, 1, player):
            return player
        
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
