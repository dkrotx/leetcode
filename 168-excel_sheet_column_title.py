class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        res = ""
        while n:
            n -= 1
            digit = n % 26
            res = chr(ord('A') + digit) + res
            n = (n - digit) // 26
            
        return res
        
# 1..26 -> A..Z
# 28
# 28 % 26 == 2, A,B
# 35: 35 % 26 = 9 (I) 35 - 9 = 26; 26/26 = 1
# 27 = 27 % 26

# 9
# 9 % 2 = 1; 9 - 1 = 8
# 
