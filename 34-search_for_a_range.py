class Solution:
    @staticmethod
    def lower_bound(arr, val):
        l, u = 0, len(arr)
        
        while l < u:
            mid = (l + u) // 2
            if arr[mid] >= val:
                u = mid
            else:
                l = mid + 1
        
        return l
    
    @staticmethod
    def upper_bound(arr, val, start):
        l, u = start, len(arr)
        
        while l < u:
            mid = (l + u) // 2
            if arr[mid] <= val:
                l = mid + 1
            else:
                u = mid
                
        return l
    
    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = Solution.lower_bound(nums, target)
        if start >= len(nums) or nums[start] != target:
            return [-1, -1]
        
        end = Solution.upper_bound(nums, target, start) - 1
        return [start, end]
