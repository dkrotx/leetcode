class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num, mul = 0, 1
        for c in reversed(s):
            num += mul * (ord(c) - ord('A') + 1)
            mul *= 26
            
        return num
