class Solution:
    @staticmethod
    def getBlockId(row, col):
        return "%d.%d" % (row // 3, col // 3)
        
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        filled = set()
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == '.':
                    continue
                    
                row_key = 'r%d:%s' % (row, val)
                col_key = 'c%d:%s' % (col, val)
                blk_key = 'b%s:%s' % (Solution.getBlockId(row, col), val)
                for k in (row_key, col_key, blk_key):
                    if k in filled:
                        return False
                    filled.add(k)
                    
        return True
