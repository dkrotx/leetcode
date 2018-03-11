class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        
        minlen = min(map(len, strs))
        n = 0
        still_equal = True
        
        while n < minlen and still_equal:
            c = strs[0][n]
            for i in range(1, len(strs)):
                if strs[i][n] != c:
                    still_equal = False
                    break
            else:
                n += 1
                
        return strs[0][:n]
