class Solution:
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        res = []
        limit = 1 << len(word)
        for var in range(limit):
            res.append(self.makeVariant(word, var))
            
        return res
    
    @staticmethod
    def makeVariant(word, mask):
        abbr = []
        n_ones = 0 # we should't produce 'w11d', but instead 'w2d'
        
        for i in reversed(range(len(word))):
            bit = mask & (1 << i)
            if bit:
                n_ones += 1
            else:
                if n_ones:
                    abbr.append(str(n_ones))
                    n_ones = 0
                abbr.append(word[-i - 1]) # take i-th letter from right side of word
                
        if n_ones:
            abbr.append(str(n_ones))
            
        return ''.join(abbr)
