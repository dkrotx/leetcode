class Solution(object):
    digits = "0123456789abcdef"
    
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            num &= (1 << 32) - 1
        
        res = ""
        while num or not res:
            digit = num % 16
            num = (num - digit) / 16
            res = Solution.digits[digit] + res
            
        return res
