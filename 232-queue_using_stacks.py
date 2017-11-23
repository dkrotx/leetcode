class MyQueue:
    def __init__(self):
        self.stk_a = []
        self.stk_b = []
        

    def push(self, x):
        self.stk_a.append(x)
        
    def _prepare_pop(self):
        if not self.stk_b:
            while self.stk_a:
                self.stk_b.append(self.stk_a.pop())

    def pop(self):
        self._prepare_pop()
        return self.stk_b.pop()

    def peek(self):
        self._prepare_pop()
        return self.stk_b[-1]        

    def empty(self):
        return not (self.stk_b or self.stk_a)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
