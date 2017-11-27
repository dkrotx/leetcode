class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, u = 0, len(nums)
        ret=nums[0]
        while l < u:
            m = (l + u) / 2
            ret = min(ret, nums[m])
            
            if nums[m] < nums[l] or nums[m] > nums[u-1]:
                if nums[m] < nums[l]:
                    u = m
                else:
                    l = m+1
            else:
                u = m
                
        return ret
