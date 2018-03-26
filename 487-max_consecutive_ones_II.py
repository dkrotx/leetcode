class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def count(i, x):
            end = i
            while end < len(nums) and nums[end] == x:
                end += 1
            return end-i, end
        
        def count_ones(i):
            return count(i, 1)
        
        def count_zeroes(i):
            return count(i, 0)
        
        if not nums:
            return 0
        
        prev_ones = max_ones = 0
        nzeroes, i = count_zeroes(0)
        
        while i < len(nums):
            cur_ones, i = count_ones(i)
            if nzeroes == 1:
                max_ones = max(prev_ones + 1 + cur_ones, max_ones)
            elif nzeroes > 0: # except the beggining
                max_ones = max(1 + cur_ones, max_ones)
            else:
                max_ones = max(cur_ones, max_ones)
                
            nzeroes, i = count_zeroes(i)
            prev_ones = cur_ones
            
        if nzeroes: # includes the case [0]
            max_ones = max(prev_ones+1, max_ones)
            
        return max_ones
