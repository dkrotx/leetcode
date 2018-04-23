class Solution {
public:
    double calcArea(int x1, int y1, int x2, int y2, int x3, int y3) {
        return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0;
    }
    
    double largestTriangleArea(vector<vector<int>>& points) {
        double max_area = 0;
        for (size_t p1 = 0; p1 < points.size() - 2; p1++) {
            for (size_t p2 = p1+1; p2 < points.size() - 1; p2++) {
                for (size_t p3 = p2+1; p3 < points.size(); p3++) {
                    max_area = max(max_area, 
                                   calcArea(points[p1][0], points[p1][1],
                                            points[p2][0], points[p2][1],
                                            points[p3][0], points[p3][1]));
                }
            }
        }
        
        return max_area;
    }
};
