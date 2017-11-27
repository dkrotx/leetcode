class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        n = 0
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 'X':
                    left = board[row][col-1] if col > 0 else '.'
                    top  = board[row-1][col] if row > 0 else '.'
                    if left == '.' and top == '.':
                        n += 1
                        
        return n
