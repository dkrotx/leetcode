class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x
        while l < r:
            num = (l + r) // 2

            if num ** 2 < x:
                l = num + 1
            else:
                r = num
        
        return l if l**2 == x else l-1
