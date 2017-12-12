class Solution(object):
    def isPerfectSquare(self, num):
        l = 0
        r = num+1
        
        while l < r:
            mid = (l + r) // 2
            square = mid ** 2
            
            if square == num:
                return True
            if square > num:
                r = mid
            else:
                l = mid+1
                
        return False
                
        """
        :type num: int
        :rtype: bool
        """
