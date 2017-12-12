class Solution(object):
    def twoSum(self, arr, x):
        nums = [(val, i) for i, val in enumerate(arr)]
        nums.sort()
    
        l = 0
        r = len(nums) - 1
    
        while l < r:
            while r > l and nums[r][0] + nums[l][0] > x:
                r -= 1
            if r > l and nums[l][0] + nums[r][0] == x:
                return sorted([nums[l][1], nums[r][1]])
            l += 1
    
        return []
