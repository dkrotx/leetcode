class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        self.height = len(obstacleGrid)
        self.width = len(obstacleGrid[0])
        
        self.grid = [[-1] * self.width for _ in range(self.height)]
        self.grid[-1][-1] = 1
        
        self.obstacle_grid = obstacleGrid
        return self.countPaths(0, 0)
    
    def can_go(self, y, x):
        return y < self.height and x < self.width and not self.obstacle_grid[y][x]
    
    def countPaths(self, y, x):
        if not self.can_go(y, x):
            return 0
            
        if self.grid[y][x] == -1:
            self.grid[y][x] = self.countPaths(y+1, x) + self.countPaths(y, x+1)

        return self.grid[y][x]
