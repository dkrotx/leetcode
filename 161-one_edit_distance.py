class Solution:
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == len(t):
            return self.exactlyOneDifferentChar(s, t)
        
        if len(s) == len(t) + 1:
            return self.canSkipOneChar(s, t)
        elif len(t) == len(s) + 1:
            return self.canSkipOneChar(t, s)
        
        return False
    
    def canSkipOneChar(self, big, small):
        assert(len(big) == len(small) + 1)
        
        skipped = False
        bi = si = 0
        for bi in range(len(big)):
            if si < len(small) and big[bi] == small[si]:
                si += 1
            else:
                # do not shift `si'
                if skipped:
                    return False
                skipped = True
        
        assert(skipped) # lenghts are different, so we should skip smthng anyway
        return True
        
    def exactlyOneDifferentChar(self, s, t):
        assert(len(s) == len(t))
        
        diff = False
        for i in range(len(s)):
            if s[i] != t[i]:
                if diff:
                    return False
                diff = True
                
        return diff
