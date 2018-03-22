class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if nums[i] != i+1:
                cur = nums[i]
                nums[i] = 0
                while cur:
                    pos = cur-1
                    if nums[pos] == cur:
                        cur = None # nowhere to place further
                    else:
                        nums[pos], cur = cur, nums[pos]
            
        return [i+1 for i in range(len(nums)) if not nums[i]]
