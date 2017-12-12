class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dc = dict()
        for c in s:
            if c in dc:
                dc[c] += 1
            else:
                dc[c] = 1
        
        for c in t:
            if c in dc:
                dc[c] -= 1
            else:
                return c
        
        for c, n in dc.items():
            if n:
                return c
            
        raise runtimeError("no difference found")
