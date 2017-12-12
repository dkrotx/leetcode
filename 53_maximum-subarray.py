class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = nums[0]
        cursum = 0
        for i in range(len(nums)):
            cursum += nums[i]
            maxsum = max(maxsum, cursum)
            if cursum < 0:
                cursum = 0 # drop previous numbers
                
        return maxsum
