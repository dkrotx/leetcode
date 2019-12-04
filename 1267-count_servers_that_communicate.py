class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        if not any(grid):
            return 0
        
        sum_by_rows, sum_by_cols = [0] * len(grid), [0] *len(grid[0])
        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                sum_by_rows[i] += value
                sum_by_cols[j] += value
        
        n = 0
        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                if value and (sum_by_rows[i] > 1 or sum_by_cols[j] > 1):
                    n += 1
                    
        return n
