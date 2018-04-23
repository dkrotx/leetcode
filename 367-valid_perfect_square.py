class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l, r = 1, num+1
        while l < r:
            mid = (l + r) // 2
            square = mid*mid
            if square == num:
                return True
            if num < square:
                r = mid
            else:
                l = mid + 1
                
        return False
