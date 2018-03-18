class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        def do_op(op, a, b):
            if op == '+': return a + b
            if op == '-': return a - b
            if op == '*': return a * b
            if op == '/': return int(a / b) # not //, because 6 // 121 == -1 (aaa!)
        
        stk = []
        for t in tokens:
            if t in '+-*/':
                stk.append(do_op(t, b=stk.pop(), a=stk.pop()))
            else:
                stk.append(int(t))
                
        assert(len(stk) == 1)
        return stk.pop()
