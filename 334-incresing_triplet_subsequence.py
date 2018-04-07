class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = mid = float('inf')
        for x in nums:
            if x <= first:
                first = x
            elif x <= mid:
                mid = x
            else:
                return True
            
        return False
