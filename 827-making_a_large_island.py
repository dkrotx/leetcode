class Solution:
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.islands = []
        self.land_cells = {}
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        
        self.discoverIslands()
        return self.tryToReplaceWater()
        
    def getNeighbors(self, row, col):
        neighbors = []
        for r,c in (row-1, col), (row+1, col), (row, col-1), (row, col+1):
            if 0 <= r < self.height and 0 <= c < self.width:
                neighbors.append((r, c))
            
        return neighbors
        
    def discoverThisIsland(self, row, col, island_id):
        assert(self.grid[row][col] == 1)
        
        # mark initial point as discovered
        frontier = [(row, col)]
        self.land_cells[(row, col)] = island_id
        size = 1
        
        while frontier:
            next_frontier = []
            for rf, cf in frontier:
                for r, c in self.getNeighbors(rf, cf):
                    if self.grid[r][c] == 1 and (r, c) not in self.land_cells:
                        self.land_cells[(r, c)] = island_id
                        next_frontier.append((r, c))
                        size += 1
                        
            frontier = next_frontier
                
        return size
        
    def tryToReplaceThisWater(self, row, col):
        assert(self.grid[row][col] == 0)
        
        merged_islands = set()
        for r, c in self.getNeighbors(row, col):
            if (r, c) in self.land_cells:
                island_id = self.land_cells[(r, c)]
                merged_islands.add(island_id)
                
        merged_size = 1 # merging point iself
        for island in merged_islands:
            merged_size += self.islands[island]
        return merged_size
        
    def discoverIslands(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] == 1 and (row, col) not in self.land_cells:
                    size = self.discoverThisIsland(row, col, island_id=len(self.islands))
                    self.islands.append(size)
                    
    def tryToReplaceWater(self):
        max_size = max(self.islands) if self.islands else 1
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] == 0:
                    max_size = max(max_size, self.tryToReplaceThisWater(row, col))
                    
        return max_size
