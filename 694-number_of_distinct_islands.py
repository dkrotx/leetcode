class Solution:
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def getNearLand(row, col):
            res = []
            nrows, ncols = len(grid), len(grid[0])
            for pt in (row-1, col),(row+1, col),(row, col-1), (row, col+1):
                if (0 <= pt[0] < nrows and 0 <= pt[1] < ncols) and grid[pt[0]][pt[1]] == 1:
                    res.append(pt)
                    
            return res
            
        def getLandMap(row0, col0):
            land = []
            frontier = [(row0, col0)]
            grid[row0][col0] = 2 # seen
            
            while frontier:
                next_frontier = []
                for pt in frontier:
                    land.append((pt[0] - row0, pt[1] - col0)) # add relative coordinate
                    
                    for near in getNearLand(*pt):
                        grid[near[0]][near[1]] = 2
                        next_frontier.append(near)
                    
                frontier = next_frontier
                
            return tuple(land)
                
                
        lands = set()
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    lands.add(getLandMap(row, col))
                    
        return len(lands)
