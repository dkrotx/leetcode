class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            negative_n = True
            n = -n
        elif n == 0:
            return 1.0
        else:
            negative_n = False
            
        pows = [1, x]
        i = 1
        while i < n:
            pows.append(pows[-1]*pows[-1])
            i *= 2
        
        res = 1.0
        i = 0
        while n:
            mask = 1 << i
            if n & mask:
                res *= pows[i+1]
                n &= ~mask
            i += 1
            
        return 1. / res if negative_n else res
