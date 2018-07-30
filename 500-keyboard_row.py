class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        self.chars = {}
        for row, letters in enumerate(["qwertyuiop", "asdfghjkl", "zxcvbnm"]):
            for c in letters:
                self.chars[c] = row
            
        return list(filter(lambda w: self.isOneRow(w), words))
        
    def isOneRow(self, word):
        common_row = None
        for c in word:
            row = self.chars[c.lower()]
            if common_row is None:
                common_row = row
            elif common_row != row:
                return False
            
        return True
