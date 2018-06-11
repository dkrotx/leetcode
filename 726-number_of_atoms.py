from collections import defaultdict

class Solution:
    @staticmethod
    def tokenize(s):
        tokens = []
        i = 0
        
        while i < len(s):
            if s[i] == '(' or s[i] == ')':
                tokens.append(s[i])
                i += 1
            elif s[i].isdigit():
                for j in range(i+1, len(s)+1):
                    if j == len(s) or not s[j].isdigit():
                        break
                tokens.append(int(s[i:j]))
                i = j
            else:
                assert(s[i].isupper())
                for j in range(i+1, len(s)+1):
                    if j == len(s) or not s[j].islower():
                        break
                tokens.append(s[i:j])
                i = j
        
        return tokens
    
    @staticmethod
    def serializeFormula(atoms):
        res = []
        for elem, n in sorted(list(atoms.items())):
            res.append(elem)
            if n > 1:
                res.append(str(n))
                
        return ''.join(res)
                
    
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        atoms = self.makeFlatSubFormula(self.tokenize(formula))[0]
        return self.serializeFormula(atoms)
    
    @staticmethod
    def mergeDicts(dst, src, repeat):
        for k, n in src.items():
            dst[k] += n * repeat
        
    def makeFlatSubFormula(self, toks, i=0):
        elems = defaultdict(int)
        
        while i < len(toks):
            if toks[i] == '(':
                sub_elems, i = self.makeFlatSubFormula(toks, i+1)
                n = 1
                if i < len(toks) and type(toks[i]) is int: # account N in "(...)N"
                    n = toks[i]
                    i += 1
                self.mergeDicts(elems, sub_elems, n)
            elif toks[i] == ')':
                i += 1
                break
            else:
                elem = toks[i]
                i += 1
                n = 1
                if i < len(toks) and type(toks[i]) is int:
                    n = toks[i]
                    i += 1
                elems[elem] += n
                
        return elems, i
