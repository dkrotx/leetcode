class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        """ move all red to beginning """
        nred = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[nred], nums[i] = nums[i], nums[nred]
                nred += 1
        
        """ move all white right after red """
        nwhite = 0
        for i in range(nred, len(nums)):
            if nums[i] == 1:
                nums[nred+nwhite], nums[i] = nums[i], nums[nred+nwhite]
                nwhite += 1
