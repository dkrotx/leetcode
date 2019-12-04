WATER = 1
LAND = 0

class ClosedIslandsCounter:
    def __init__(self, grid: List[List[int]]):
        self.visited = set()
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        
    def solve(self):
        n = 0
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] == LAND and (row, col) not in self.visited:
                    if self._discover_island(row, col):
                        n += 1
                        
        return n
                        
    def _get_neighbors(self, row, col):
        neighbors = set()
        
        for r, c in (row, col-1), (row, col+1), (row-1, col), (row+1, col):
            if 0 <= r < self.height and 0 <= c < self.width and self.grid[r][c] == LAND:
                neighbors.add((r, c))
                
        return neighbors
    
    def _at_the_edge(self, row, col):
        return row == 0 or col == 0 or col == self.width - 1 or row == self.height-1
                        
    def _discover_island(self, row, col):
        is_closed = True
        frontier = {(row, col)}
        
        while frontier:
            new_frontier = set()
            for pt in frontier:
                if pt in self.visited:
                    continue
                self.visited.add(pt)
                
                if self._at_the_edge(pt[0], pt[1]):
                    is_closed = False
                    
                new_frontier |= self._get_neighbors(pt[0], pt[1])
                
            frontier = new_frontier
            
        return is_closed
        

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not any(grid):
            return 0
        
        return ClosedIslandsCounter(grid).solve()
