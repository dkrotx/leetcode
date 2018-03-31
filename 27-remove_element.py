class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        iw = 0
        for x in nums:
            if x != val:
                nums[iw] = x
                iw += 1
                
        return iw
