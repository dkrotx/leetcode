struct GridContext {
    const vector<vector<int>>& grid;
    vector<vector<unsigned>> known_mins;
    int height;
    int width;
    
    GridContext(const vector<vector<int>>& a_grid) : grid(a_grid) {
        height = grid.size();
        width = height ? grid[0].size() : 0;
        init_known_mins();
    }
    
    inline bool is_bottom(int y) const { return y == height-1; }
    inline bool is_right(int x)  const { return x == width-1;  }
    
    inline bool unknown_min(int x, int y) const {
        return known_mins[y][x] == -1U;
    }
    
    bool empty() const {
        return height == 0 || width == 0;
    }
    
    private:
        void init_known_mins() {
            vector<unsigned> row(width, -1U);
            for (int i = 0; i < height; i++)
                known_mins.push_back(row);
        }
};

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
       GridContext ctx(grid);
       return (ctx.empty()) ? 0 : find_min_path(ctx, 0, 0);
    }
    
    unsigned find_min_path(GridContext &ctx, int x, int y) 
    {
        if (ctx.unknown_min(x, y)) {
            unsigned further_len;
            
            if (ctx.is_bottom(y) && ctx.is_right(x)) {
                further_len = 0;
            } else {
                unsigned sum_bottom = -1U, sum_right  = -1U;
                
                if (!ctx.is_bottom(y))
                    sum_bottom = find_min_path(ctx, x, y+1);
                if (!ctx.is_right(x))
                    sum_right  = find_min_path(ctx, x+1, y);
                
                further_len = min(sum_bottom, sum_right);
            }
            
            ctx.known_mins[y][x] = ctx.grid[y][x] + further_len;
        }
        return ctx.known_mins[y][x];
    }
};
