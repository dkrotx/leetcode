class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace('-', '').upper()
        first = len(S) % K if len(S) % K > 0 else K
        res = S[:first]
        
        for i in range(first, len(S), K):
            res += '-'
            res += S[i:i+K]
            
        return res
