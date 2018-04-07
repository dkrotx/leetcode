class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start, max_len = 0, 0
        chars = set()
        
        for i, ch in enumerate(s):
            while ch in chars:
                chars.remove(s[start])
                start += 1
                
            chars.add(ch)
            max_len = max(max_len, i - start + 1)
            
        return max_len
