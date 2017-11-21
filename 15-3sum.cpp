#include <vector>
#include <algorithm>

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        
        if (nums.size() < 3)
            return res;
        
        sort(nums.begin(), nums.end());
        
        int ia = 0;
        while(ia < nums.size() - 2) {
            int a = nums[ia];
            int ib = ia + 1;
            int last_ic = nums.size();
            while (ib < nums.size() - 1) {
                int b = nums[ib];
                int c = -(a + b);
                
                // it works faster than hash-table of 'c'
                auto it_c = lower_bound(nums.begin() + ib + 1, nums.begin() + last_ic, c);
                if (it_c != nums.end() && *it_c == c) {
                    vector<int> v = {a, b, c};
                    res.push_back(v);
                }
                
                // since b will grow up, a+b will grow too. And we need lower value of 'c'
                last_ic = distance(nums.begin(), it_c);
                
                for(++ib; ib < nums.size() && nums[ib] == b; ib++) {}
            }
            
            for(++ia; ia < nums.size() && nums[ia] == a; ia++) {}
        }
        
        return res;
    }
};
