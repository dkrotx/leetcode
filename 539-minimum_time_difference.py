class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        minutes = list(map(Solution.time2mins, timePoints))
        minutes.sort()
        min_diff = minutes[0] + 24*60 - minutes[-1]
        
        for i in range(len(minutes)-1):
            min_diff = min(min_diff, minutes[i+1] - minutes[i])
            
        return min_diff
    
    @staticmethod
    def time2mins(s):
        hrs, mins = map(int, s.split(':'))
        return hrs * 60 + mins
