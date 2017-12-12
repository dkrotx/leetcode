class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        mask=0b101010101010101010101010101010101010101
        if num and (num & (num -1)) == 0 and num & mask:
            return True
            
        return False
