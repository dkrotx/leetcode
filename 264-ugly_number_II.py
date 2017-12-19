import sys
from heapq import *

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = None
        frontier = set()
        h = [1]

        for _ in range(n):
            x = heappop(h)

            for mul in (2,3,5):
                v = mul * x
                if v not in frontier:
                    heappush(h, v)
                    frontier.add(v)

        return x
