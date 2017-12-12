class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator == 0:
            return "inf"
        
        if numerator != 0 and (numerator < 0) ^ (denominator < 0):
            s = "-"
        else:
            s = ""
            
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        s += str(numerator // denominator)
        mod = numerator % denominator
        
        if mod:
            s += "." + Solution.calc_after_point(mod, denominator)
        
        return s
    
    @staticmethod
    def calc_after_point(mod, denominator):
        mod_track = dict()
        digits = []
        period_start = None
        
        while mod:
            if mod in mod_track:
                # we will get same sequence of digits anyway
                # for example 1/3 = 0.(3), 1/7 is 0.(142857)
                period_start = mod_track[mod]
                break
            
            mod_track[mod] = len(digits)
            
            mod *= 10
            digit = mod // denominator
            mod %= denominator
            
            digits.append(digit)
            
        
        if period_start is None:
            res = ''.join([str(d) for d in digits])
        else:
            res = ''.join([str(d) for d in digits[:period_start]])
            res += '(%s)' % ''.join([str(d) for d in digits[period_start:]])

        return res
