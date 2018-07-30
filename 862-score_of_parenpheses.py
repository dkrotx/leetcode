class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        self.pos = 0
        self.s = S
        return self.countScore()
    
    def countScore(self):
        total = 0
        
        while self.pos < len(self.s):
            c = self.s[self.pos]
            self.pos += 1
            if c == '(':
                total += self.countScore()
            else:
                return total * 2 if total else 1
        
        return total
