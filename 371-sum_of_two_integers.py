from ctypes import c_int

class Solution(object):
    def getSum(self, a, b):
        res = 0
        e = 0
        for bit in range(32):
            a_bit = (a >> bit) & 1
            b_bit = (b >> bit) & 1
            res_bit = a_bit ^ b_bit ^ e
            e = (a_bit & b_bit) | e & (a_bit | b_bit)
            res |= res_bit << bit
        
        return c_int(res).value

# 01
# 10
# a  b   res e
# 1  0   1   0
# 0  1   11   0

# 11
# 11
# a b res e
# 1 1   0 1
# 1 1   1 1
# 0 0   1 0
# 0 0     0
