import re

class RPNBuilder:
    _available_ops = { '+': 1, '-': 1 }
    _tokenizer = re.compile(r'\d+|[\(\)\+\-]')
    
    def __init__(self, expr):
        self.expr = expr
        self.output = []
        self.operators = []
        
    @staticmethod
    def get_operator_prio(op):
        return RPNBuilder._available_ops[op]
        
    @staticmethod
    def is_operator(char):
        return char in RPNBuilder._available_ops
        
    def pop_operator(self):
        top = self.operators.pop()
        self.output.append(top[0])
        
    def push_operator(self, op, depth):
        prio = RPNBuilder.get_operator_prio(op)
        
        # pop all operators within same level (depth) having less or equal priority
        while self.operators:
            top = self.operators[-1]
            if top[1] == depth and top[2] <= prio:
                self.pop_operator()
            else:
                break
                  
        self.operators.append((op, depth, prio))
        
    def drain_operators(self, depth):
        while self.operators and self.operators[-1][1] == depth:
            self.pop_operator()
    
    def parse(self):
        depth = 0
        tokens = RPNBuilder._tokenizer.findall(self.expr)
        
        for tok in tokens:
            if RPNBuilder.is_operator(tok):
                self.push_operator(tok, depth)
            elif tok == '(':
                depth += 1
            elif tok == ')':
                self.drain_operators(depth)
                depth -= 1
            else:
                self.output.append(int(tok))
        
        assert depth == 0
        self.drain_operators(depth)
        return self.output
                

class Solution(object):
    def calculate(self, s):
        rpn = RPNBuilder(s).parse()
        return Solution._calc_rpn(rpn)
        
    @staticmethod
    def apply_operator(op, a, b):
        if (op == '+'): return a + b
        if (op == '-'): return a - b
        
    @staticmethod
    def _calc_rpn(rpn):
        stack = []
        for token in rpn:
            if type(token) is int:
                stack.append(token)
            else:
                b, a = stack.pop(), stack.pop()
                stack.append(Solution.apply_operator(token, a, b))
                
        assert len(stack) == 1
        return stack[-1]
