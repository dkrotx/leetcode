class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        s = s.lstrip()
        if not s:
            return 0
            
        i = 0
        sign = 1
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1
            
        num = 0
        for i in range(i, len(s)):
            if s[i] >= '0' and s[i] <= '9':
                num = num * 10 + ord(s[i]) - ord('0')
            else:
                break
                
        MIN_VALUE=-2147483648
        MAX_VALUE=2147483647
        
        num *= sign
        
        if num < MIN_VALUE:
            return MIN_VALUE
        if num > MAX_VALUE:
            return MAX_VALUE
        
        return num
