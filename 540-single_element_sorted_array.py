class Solution(object):
    def singleNonDuplicate(self, nums):
        l, u = 0, len(nums)
        while l + 1 < u:
            mid = (l + u) / 2
            if mid % 2:
                mid -= 1
            
            """ idea is following:
                If two elements at [i(even)][i+1] are equal, 
                then single element somewere right.
            """
            if nums[mid] == nums[mid+1]:
                l = mid + 2
            else:
                u = mid
                
        return nums[l]
