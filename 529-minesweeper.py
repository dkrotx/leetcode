class Solution:
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        cy, cx = click
        if board[cy][cx] == 'M':
            board[cy][cx] = 'X'
            return board
        
        height, width = len(board), len(board[0])
        
        def validCoord(y, x):
            return (0 <= y < height) and (0 <= x < width)
        
        def countMines(y, x):
            total = 0
            for r in range(y-1, y+2):
                for c in range(x-1, x+2):
                    if validCoord(r, c):
                        total += 1 if board[r][c] == 'M' else 0
                        
            return total
        
        def count2BoardCell(n):
            if n == 0:
                return 'B'
            return str(n)
        
        def dfsAndMark(y, x):
            n = countMines(y, x)
            board[y][x] = count2BoardCell(n)
            if n != 0:
                return
            # continue with neighbors only if no mines here
            for r in range(y-1, y+2):
                for c in range(x-1, x+2):
                    if validCoord(r, c) and board[r][c] == 'E':
                        dfsAndMark(r, c)
        
        dfsAndMark(cy, cx)
        return board
