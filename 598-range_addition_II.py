class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        maxrange = 40001  
        min_a, min_b = maxrange, maxrange
        for a, b in ops:
            if a and b:
                min_a = min(a, min_a)
                min_b = min(b, min_b)
                
        return m*n if min_a == maxrange else min_a * min_b
