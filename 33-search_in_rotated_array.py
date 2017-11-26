class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, u = 0, len(nums)
        while l < u:
            i = (l + u) / 2
            if nums[i] == target:
                return i
            if (nums[i] > nums[0] and (target < nums[i] and target >= nums[0])) or \
               (nums[i] < nums[0] and (target < nums[i] or  target >= nums[0])):
                u = i
            else:
                l = i+1
                
        return -1
