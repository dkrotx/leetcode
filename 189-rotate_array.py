from collections import deque

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        if not nums or not k:
            return
        
        fifo = deque(nums[:k], maxlen=abs(k))
        for i in range(len(nums)):
            new_i = (i + k) % len(nums)
            oldval = nums[new_i]
            nums[new_i] = fifo[0]
            fifo.append(oldval)
        
# 1 2 3 4 5 6
# - - 1 2

 
