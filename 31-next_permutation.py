class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        """
        algorithm is ('1 3 2' as input):
        - moving from right to left, look for first digit which is lower than right (1)
        - select next (nearest) number (2)
        - swap 1 and 2, '2 3 1'
        - since we switched position ([0]) sort right subarray ([1:])
          we will get '2 1 3' as result
        """
        pos = None
        for i in reversed(range(len(nums)-1)):
            if nums[i] < nums[i+1]:
                pos = i
                break
        else:
            nums.sort()
            return
        
        nextmin = pos+1
        for i in range(pos+2, len(nums)):
            if nums[i] > nums[pos] and nums[i] < nums[nextmin]:
                nextmin = i
                
        nums[pos], nums[nextmin] = nums[nextmin], nums[pos]
        nums[pos+1:] = sorted(nums[pos+1:])
