class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        openers = "({["
        closers = ")}]"
        for c in s:
            if c in openers:
                stk.append(c)
            else:
                if not stk:
                    return False
                opener_id = openers.index(stk.pop())
                if c != closers[opener_id]:
                    return False
                
        return not stk
