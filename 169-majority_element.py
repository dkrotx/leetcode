class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mem_x, mem_cnt = nums[0], 1
        for x in nums[1:]:
            if mem_x == x:
                mem_cnt += 1
            else:
                if mem_cnt == 1:
                    mem_x = x
                else:
                    mem_cnt -= 1
        
        return mem_x
