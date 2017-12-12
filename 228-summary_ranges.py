class Solution:
    @staticmethod
    def appendResult(res, start, end):
        if end == start:
            res.append(str(start))
        else:
            res.append("%d->%d" % (start, end))
                    
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        
        res = []
        start = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]+1:
                Solution.appendResult(res, start, nums[i-1])
                start = nums[i]
                
        Solution.appendResult(res, start, nums[-1])
        return res
