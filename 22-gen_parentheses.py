class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def gen(n_openers, depth):
            if n_openers == 0 and depth == 0:
                return ['']
            
            res=[]
            if n_openers:
                for v in gen(n_openers - 1, depth + 1):
                    res.append('(' + v)
                    
            if depth > 0:
                for v in gen(n_openers, depth - 1):
                    res.append(')' + v)
                    
            return res
                
        return gen(n, 0)
