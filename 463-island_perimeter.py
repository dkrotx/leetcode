class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        def within_borders(pt):
            return 0 <= pt[0] < len(grid) and 0 <= pt[1] < len(grid[0])
        
        def is_water(pt):
            return not within_borders(pt) or grid[pt[0]][pt[1]] == 0
        
        def get_neighbors(pt):
            return list(filter(within_borders, 
                               [(pt[0]-1, pt[1]), (pt[0]+1, pt[1]), 
                                (pt[0], pt[1]-1), (pt[0], pt[1]+1)]))
            
        
        perimeter = 0
        height, width = len(grid), len(grid[0])
        
        """
        The idea is to count land neigbors for every cell of water.
        For simplicity also include water cells around the grid.
        """
        for row in range(-1, height+1):
            for col in range(-1, width+1):
                if not is_water((row, col)):
                    continue
                
                for pt in get_neighbors((row, col)):
                    if grid[pt[0]][pt[1]] == 1:
                        perimeter += 1
                        
        return perimeter
