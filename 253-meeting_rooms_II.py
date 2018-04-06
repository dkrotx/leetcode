# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key=lambda x: x.start)
        
        rooms = []
        for period in intervals:
            for r in rooms:
                if not r or r[-1].end <= period.start:
                    r.append(period)
                    break
            else:
                rooms.append([period])
                
        return len(rooms)
