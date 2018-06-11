class Solution {
public:
    string reverseString(string s) {
        string res;
        for(auto it = s.rbegin(); it != s.rend(); ++it)
            res += *it;
        
        return res;
    }
};
