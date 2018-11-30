class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        hours, mins = map(int, time.split(':'))
        symbols = set([c for c in time])
        while True:
            mins += 1
            if mins == 60:
                mins = 0
                hours += 1
                if hours == 24:
                    hours = 0
                    
            clock = "%02d:%02d" % (hours, mins)
            for c in clock:
                if not c in symbols:
                    break
            else:
                return clock
        
        # impossible for any valid input
        assert False
