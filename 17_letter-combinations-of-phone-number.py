class Solution:
    letters = { 
                '2': 'abc', '3': 'def', 
                '4': 'ghi', '5': 'jkl', 
                '6': 'mno', '7': 'pqrs', 
                '8': 'tuv', '9': 'wxyz'
               }
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        strs = []
        for d in digits:
            if d in Solution.letters:
                strs.append(Solution.letters[d])
        
        combinations = []
        if strs:
            self.allCombinations(combinations, strs)
        return combinations
    
    def allCombinations(self, combinations, strs, prefix = '', i = 0):
        if i == len(strs):
            combinations.append(prefix)
        else:
            for c in strs[i]:
                self.allCombinations(combinations, strs, prefix + c, i+1)
