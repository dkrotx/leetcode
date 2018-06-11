class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        ndigits = max(len(a), len(b))
        res = []
        
        for i in range(1, ndigits+1):
            d_a = int(a[-i]) if len(a) >= i else 0
            d_b = int(b[-i]) if len(b) >= i else 0
            d_r = d_a + d_b + carry
            
            carry = 1 if d_r > 1 else 0
            d_r = d_r % 2
            res.append(d_r) 
            
        if carry:
            res.append(1) 
            
        return ''.join(map(str, reversed(res)))
