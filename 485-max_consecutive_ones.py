class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = cur_sum =  0
        for x in nums:
            if x:
                cur_sum += 1
            else:
                max_sum = max(cur_sum, max_sum)
                cur_sum = 0
                
        return max(cur_sum, max_sum)
