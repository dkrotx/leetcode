from collections import defaultdict

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words_len = []
        self.len_variats = set() # for cases of search('....') (only dots) 
        self.word2id = dict()
        self.pos_chars = defaultdict(set)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if word in self.word2id:
            return
        
        wid = len(self.words_len)
        self.word2id[word] = wid
        self.words_len.append(len(word))
        self.len_variats.add(len(word))
        
        for pos, c in enumerate(word):
            self.pos_chars[(pos, c)].add(wid)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        ndots = 0
        for c in word:
            if c == '.':
                ndots += 1
       
        """ handle easy cases: no dots, and while search of dots """
        if ndots == 0:
            return word in self.word2id
        if ndots == len(word):
            return len(word) in self.len_variats
        
        candidates = []
        for pos, c in enumerate(word):
            if c == '.':
                continue
                
            if (pos, c) not in self.pos_chars:
                return False # some character not found
            
            same_len_words = set(
                filter(lambda wid: self.words_len[wid] == len(word), self.pos_chars[(pos, c)])
            )
            candidates.append(same_len_words)
            
        """
        Make a conjunction between letters on positions
        Speedup: move shortest list of candidates to beginning
        """ 
        candidates.sort(key=lambda ids: len(ids))
        
        res = candidates[0]
        for cand in candidates[1:]:
            res &= cand
            
        return bool(res)
                


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
