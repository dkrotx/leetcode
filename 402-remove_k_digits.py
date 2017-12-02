class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        digits = []
        for c in num:
            while k and digits and digits[-1] > c:
                digits.pop()
                k -= 1
                
            if digits or c != '0':
                digits.append(c)
                
        while digits and k:
            digits.pop()
            k -= 1
                
        res = ''.join(digits)
        return res if res else "0"
