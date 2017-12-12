class Solution(object):
    @staticmethod
    def decode_n(c):
        n = 0
        for n in range(5):
            if c & (1 << (7-n)) == 0:
                return n
        return -1
            
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        rest_n = 0
        for b in data:
            if rest_n:
                if b >> 6 != 0b10:
                    return False
                rest_n -= 1
            else:
                if b >= 128:
                    rest_n = self.decode_n(b)
                    if rest_n < 2 or rest_n > 4:
                        return False
                    rest_n -= 1
        
        return rest_n == 0
