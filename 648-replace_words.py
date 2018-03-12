class PrefixTree:
    class Node:
        def __init__(self, val):
            self.value = val
            self.final = False
            self.childs = dict()   
        
    def __init__(self):
        self.root = PrefixTree.Node('^')
        
    def addUniqueWord(self, word):
        node = self.root
        for c in word:
            if node.final:
                return False # already have this prefix as final word
            if c not in node.childs:
                node.childs[c] = PrefixTree.Node(c)
            node = node.childs[c]
            
        node.final = True
        return True
    
    def findPrefixFor(self, word):
        node = self.root
        for i, c in enumerate(word):
            if node.final:
                return word[:i]
            
            if c in node.childs:
                node = node.childs[c]
            else:
                break
                
        return None

class Solution:    
    def replaceWords(self, dictionary, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        prefix_tree = PrefixTree()
        """ Add words from shortest ones - to meet this requirement:
            If a successor has many roots can form it, replace it with the root with the shortest length.
        """
        for w in sorted(dictionary, key=lambda s: len(s)):
            prefix_tree.addUniqueWord(w)
            
        words = sentence.split()
        res = []
        for w in words:
           res.append(prefix_tree.findPrefixFor(w) or w)
        
        return ' '.join(res)
