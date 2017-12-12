struct Grid {
    vector<vector<char>> grid;
    int width;
    int height;
    
    Grid(const vector<vector<char>>& a_grid) : grid(a_grid) {
        height = grid.size();
        width  = (height > 0) ? grid[0].size() : 0;
    }
    
    char get(int x, int y) const {
        if (x >= 0 && x < width && y >= 0 && y < height)
            return grid[y][x];
        return '0';
    }
    
    void set(int x, int y, char val) {
        grid[y][x] = val;
    }
};

class Solution {
public:
    int numIslands(vector<vector<char>>& vector_grid) {
        int  n = 0;
        Grid grid(vector_grid);

        for(int y = 0; y < grid.height; y++)
            for(int x = 0; x < grid.width; x++) {
                if (grid.grid[y][x] == '1') {
                    discover_land(grid, x, y);
                    n++;
                }
            }
        
        return n;
    }
    
    void discover_land(Grid& grid, int x, int y) {
        if (grid.get(x, y) == '1') {
            grid.set(x, y, '2');
            discover_land(grid, x-1, y);
            discover_land(grid, x+1, y);
            discover_land(grid, x, y-1);
            discover_land(grid, x, y+1);
        }
    }
};
