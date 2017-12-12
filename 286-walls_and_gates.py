class Solution:
    INF = 2147483647
    
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not any(rooms): return
        
        nrows = len(rooms)
        ncols = len(rooms[0])
        stk = []
        for r, row in enumerate(rooms):
            for c, val in enumerate(row):
                if not val:
                    stk.append((r, c))
                    
        distance = 1
        while stk:
            frontier = []
            for r, c in stk:
                for rn, cn in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)):
                    if 0 <= rn < nrows and 0 <= cn < ncols and rooms[rn][cn] == Solution.INF:
                        rooms[rn][cn] = distance
                        frontier.append((rn, cn))
            
            stk = frontier
            distance += 1
