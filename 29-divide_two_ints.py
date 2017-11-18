class Solution(object):
    def divide_positives(self, a, b):
        """ Solution to divide a/b is:
            - fill power of 2 of b (using sum)
            - substract this values from a
              and adding N
            
            This looks like expressing a in "b-ary" system.
            It will take O(1) since up to ndigits(int)
        """
        b_pows = []
        cur_sum, cur_n = b, 1
        
        while cur_sum <= a:
            b_pows.append((cur_sum, cur_n))
            cur_sum += cur_sum
            cur_n += cur_n
        
        res = 0
        for digit in reversed(b_pows):
            if a >= digit[0]:
                a -= digit[0]
                res += digit[1]
                
        return res

	def account_int_overflow(self, x):
        return (1 << 31) - 1 if x >= 1 << 31 else x
        
    def divide(self, a, b):
        if not b:
            raise ZeroDivisionError("Attempt to divide to zero");
            
        sign = False
        if a < 0:
            sign = not sign
            a = -a
        if b < 0:
            sign = not sign
            b = -b
            
        res = self.divide_positives(a, b)
        if sign:
            res = -res
        
		return self.account_int_overflow(res)
