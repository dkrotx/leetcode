class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def maxPalindrome(a, b):
            while a >= 0 and b < len(s) and s[a] == s[b]:
                a -= 1
                b += 1
                
            return s[a+1:b]
        
        if len(s) <= 1:
            return s
        
        best = ''
        for i in range(len(s)):
            for pal in maxPalindrome(i, i+1), maxPalindrome(i-1, i+1):
                if len(pal) > len(best):
                    best = pal
            
        return best
