class Solution:
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        def rangeStr(start, end):
            if start == end:
                return str(start)
            return "%d->%d" % (start, end)
        
        ret = []
        expect = lower
        for x in nums:
            if x > expect:
                ret.append(rangeStr(expect, x-1))
            expect = x + 1
            
        if expect <= upper:
            ret.append(rangeStr(expect, upper))
            
        return ret
