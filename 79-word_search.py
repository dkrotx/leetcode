class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not word:
            return False
        
        self.board = board
        self.word = word
        self.nrows = len(board)
        self.ncols = len(board[0])
        self.used = [[0]*self.ncols for _ in range(self.nrows)]
        
        for row in range(self.nrows):
            for col in range(self.ncols):
                if self.lookup(row, col):
                    return True
                
        return False
                
    def lookup(self, row, col, i=0):
        if i == len(self.word):
            return True
        
        if 0 <= row < self.nrows and 0 <= col < self.ncols \
           and self.board[row][col] == self.word[i] and not self.used[row][col]:
                self.used[row][col] = 1
                for near in (row-1,col),(row+1, col),(row, col-1),(row, col+1):
                    if self.lookup(near[0], near[1], i+1):
                        return True
                self.used[row][col] = 0
        
        return False
