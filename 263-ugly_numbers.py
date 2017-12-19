class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0: return False
        while num > 1:
            for u in (2, 3, 5):
                if num % u == 0:
                    num //= u
                    break
            else:
                return False
            
        return True
