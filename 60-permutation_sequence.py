import math

class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k -= 1 # easier to deal with 0-based
        items = list(map(str, range(1, n+1)))
        res = []
        
        while items:
            perms_but_one = math.factorial(len(items) - 1)
            i = k // perms_but_one
            res.append(items[i])
            del items[i]
            k %= perms_but_one
        
        return ''.join(res)
