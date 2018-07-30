from collections import defaultdict

class ValidWordAbbr:

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.abbrevs = defaultdict(set)
        
        for word in dictionary:
            self.abbrevs[self.abbreviation(word)].add(word)
    
    @staticmethod
    def abbreviation(word):
        if len(word) < 3:
            return word
        
        return '%c%d%c' % (word[0], len(word) - 2, word[-1])

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        abbr = self.abbreviation(word)
        if abbr in self.abbrevs:
            abbr_set = self.abbrevs[abbr]
            if len(abbr_set) > 1 or word not in abbr_set:
                return False
            
        return True


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
