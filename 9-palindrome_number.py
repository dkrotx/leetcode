class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        def get_digit(i):
            return (x % 10**i) // 10**(i-1)
        
        def ndigits(i):
            n = 1
            while i >= 10 ** n:
                n += 1
                
            return n
                
        if x < 0:
            return False
        
        nl, nh = 1, ndigits(x) # _high_ and _low_ digit
        
        while nh > nl:
            if get_digit(nh) != get_digit(nl):
                return False
            nh -= 1
            nl += 1
            
        return True
