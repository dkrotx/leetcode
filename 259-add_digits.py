class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if not num:
            return 0
        
        digsum = 0
        while num:
            digsum += num % 10
            num //= 10
            
        return digsum % 9 or 9
        
