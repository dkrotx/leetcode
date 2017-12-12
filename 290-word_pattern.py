class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = s.split()
        
        if len(words) != len(pattern):
            return False
        
        matching = dict()
        used_patterns = set()
        
        for word, pat in zip(words, pattern):
            if word in matching:
                if matching[word] != pat:
                    return False
            else:
                if pat in used_patterns:
                    return False # already used this for another word
                matching[word] = pat
                used_patterns.update([pat])
                
        return True
        
# dog -> 'a'
# cat 
