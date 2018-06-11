class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.grid = [[0]*n for _ in range(m)]
        self.height = m
        self.width = n
        self.grid[m-1][n-1] = 1
        return self.countPaths(0, 0)
        
    def countPaths(self, y, x):
        if y >= self.height or x >= self.width:
            return 0
        
        if not self.grid[y][x]:
            self.grid[y][x] = self.countPaths(y+1, x) + self.countPaths(y, x+1)
            
        return self.grid[y][x]
