import re

class RPNMaker(object):
    def __init__(self, s):
        self.input_expr = s
        self.operators = []
        self.output = []
        self.ops_prio = {'/': 2, '*': 2, '+': 1, '-': 1}
        
    def get_priority(self, op):
        if op in self.ops_prio:
            return self.ops_prio[op]
        return None
    
    def is_operator(self, char):
        return self.get_priority(char) is not None
    
    def _push_operator(self, op):
        this_prio = self.get_priority(op)
        while self.operators and this_prio <= self.get_priority(self.operators[-1]):
            self.output.append(self.operators.pop())
        
        self.operators.append(op)
        
    def _operators2output(self):
        while self.operators:
            self.output.append(self.operators.pop())
        
    def parse(self):
        if self.output:
            return self.output
            
        tokens = re.findall(r'\d+|[\*\/\+\-]', self.input_expr)
        for tok in tokens:
            if self.is_operator(tok):
                self._push_operator(tok)
            else:
                self.output.append(int(tok))
                
        self._operators2output()
        return self.output


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        rpn = RPNMaker(s).parse()
        return Solution.eval_rpn(rpn)
        
    @staticmethod
    def apply_operation(op, a, b):
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b
        if op == '/':
            return a // b
    
    @staticmethod
    def eval_rpn(rpn):
        stack = []
        
        for token in rpn:
            if type(token) is int:
                stack.append(token)
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(Solution.apply_operation(token, a, b))
        
        assert len(stack) == 1
        return stack.pop()
