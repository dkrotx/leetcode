class Solution:
    def getFactors(self, n, start=2):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        i = start
        while i*i <= n:
            if n % i == 0:
                num = n // i
                res.append([i, num])
                for subvar in self.getFactors(num, i):
                    res.append([i] + subvar)
            i += 1
        
        return res
