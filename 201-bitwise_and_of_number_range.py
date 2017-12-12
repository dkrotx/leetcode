class Solution(object):
    def rangeBitwiseAnd1(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        x = m & n
        
        for ibit in range(32):
            val = 1 << ibit
            if m & val:
                if m + val > n:
                    break
                
                x &= ~val # clear single bit
                m &= ~val
            
        return x
        
    def rangeBitwiseAnd(self, m, n):
        nshifts = 0
        while m != n:
            m >>= 1
            n >>= 1
            nshifts += 1
        
        return n << nshifts
        
# 5=101 7=111
# x = 101
# ---------------
# ibit val  x    m
# 0    1    100  6
# 1    2    100  

# 0110 
# 6=0110 12=1100
# x = 0100
# ---------------
# ibit val  x    m
# 0     1   -    6
# 1     2   100  8
# 2     4   0    10
# 3


