class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            if m < len(nums)-1 and nums[m+1] > nums[m]:
                l = m + 1
            else:
                r = m
                
        return l
