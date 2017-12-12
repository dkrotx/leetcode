class Solution(object):
    def reverse(self, x):
        if x < 0:
            x = -x
            sign = -1
        else:
            sign = 1
            
        res = 0
        while x > 0:
            res *= 10
            digit = x % 10
            res += digit
            x = (x - digit) / 10
        
        if res > 2**31:
            return 0
            
        return sign * res
