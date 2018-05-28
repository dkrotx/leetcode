from collections import defaultdict

class Node:
    def __init__(self):
        self.childs = defaultdict(Node)

class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.childs[c]
        
    def hasPrefix(self, word):
        node = self.root
        for c in word:
            if c not in node.childs:
                return False
            node = node.childs[c]
            
        return True

class Solution:
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        s = ""
        trie = Trie()
        for w in sorted(words, key=lambda w: len(w), reverse=True):
            rw = ''.join(reversed(w))
            if not trie.hasPrefix(rw):
                trie.insert(rw)
                s += w + '#'
                
        return len(s)
