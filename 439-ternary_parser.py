class Node:
    def __init__(self, val):
        self.val = val
        self.positive, self.negative = None, None
        
    def isCondition(self):
        return self.positive is not None # negative should be too since expression is always correct
    
    def getConditionResult(self):
        return self.positive if self.val == 'T' else self.negative

class Solution:
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        return self.evalExpression(self.parseExprsession(expression))
    
    def parseExprsession(self, expr):
        return self.realParseExprsession(expr, 0)[0]
    
    def realParseExprsession(self, expr, i):
        node = Node(expr[i])
        i += 1

        if i < len(expr) and expr[i] == '?':
            node.positive, i = self.realParseExprsession(expr, i+1) # we are at '?' now
            assert(expr[i] == ':')
            node.negative, i = self.realParseExprsession(expr, i+1)
            
        return node, i
            
        
    def evalExpression(self, node):
        while node.isCondition():
            node = node.getConditionResult()
            
        return node.val
