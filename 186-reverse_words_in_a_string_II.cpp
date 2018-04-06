class Solution {
public:
    void reverseWords(vector<char>& str) {
        if (str.empty())
            return;
        
        size_t wstart = 0;
        for (size_t i = 0; i < str.size(); ++i) {
            if (str[i] == ' ') {
                reverseStr(&str[wstart], &str[i-1]);
                wstart = i+1;
            }
        }
        
        // reverse the last word
        reverseStr(&str[wstart], &str[str.size()-1]);
        
        // now reverse the whole string - we will got all the words reverted
        reverseStr(&str[0], &str[str.size()-1]);
    }
    
private:
    void reverseStr(char *start, char *end)
    {
        for (; start < end; start++, end--)
        {
            char t = *start;
            *start = *end;
            *end = t;
        }
    }
};
