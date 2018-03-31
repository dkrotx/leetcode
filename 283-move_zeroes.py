class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        iw  = 0
        for x in nums:
            if x:
                nums[iw] = x
                iw += 1
                
        for iw in range(iw, len(nums)):
            nums[iw] = 0
