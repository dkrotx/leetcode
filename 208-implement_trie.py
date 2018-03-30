from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.childs = defaultdict(TrieNode)

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode() # empty node, like '^'
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            node = node.childs[c]
        
        node.is_word = True
        
    def _getPrefixNode(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.childs:
                return None
            
            node = node.childs[c]
            
        return node

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self._getPrefixNode(word)
        return bool(node and node.is_word)

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self._getPrefixNode(prefix) != None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
