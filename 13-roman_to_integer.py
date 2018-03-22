class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        
        for i in range(len(s)):
            val = roman[s[i]]
            res += val if i+1 == len(s) or val >= roman[s[i+1]] else -val
            
        return res
