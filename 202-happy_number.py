class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def sum_sqr_digits(x):
            dsum = 0
            while x:
                dsum += (x % 10) ** 2
                x //= 10

            return dsum

        seen = set()

        while n not in seen:
            seen.add(n)
            n = sum_sqr_digits(n)
            if n == 1:
                return True

        return False
