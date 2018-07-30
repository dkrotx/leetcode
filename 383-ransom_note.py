from collections import defaultdict

class Solution:
    @staticmethod
    def countLetters(s):
        letters = defaultdict(int)
        for c in s:
            letters[c] += 1
        return letters
    
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom_letters = self.countLetters(ransomNote)
        mag_letters = self.countLetters(magazine)
        
        for c, n in ransom_letters.items():
            if c not in mag_letters or mag_letters[c] < n:
                return False
            
        return True
