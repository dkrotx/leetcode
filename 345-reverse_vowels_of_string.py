class Solution(object):
    vowels = set('aeiouAEIOU')
    
    @staticmethod
    def _is_vowel(char):
        return char in Solution.vowels
        
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        l = -1
        r = len(s)
        
        while l < r:
            l += 1
            while l < r and not Solution._is_vowel(s[l]):
                l += 1
                
            r -= 1
            while r > l and not Solution._is_vowel(s[r]):
                r -= 1
                
            if l < r:
                s[l], s[r] = s[r], s[l]
                
        return ''.join(s)
