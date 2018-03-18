# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        
        intervals.sort(key=lambda i: i.start)
        res = [intervals[0]]
        
        for it in intervals[1:]:
            if it.start <= res[-1].end:
                res[-1].end = max(res[-1].end, it.end)
            else:
                res.append(it)
            
        return res
