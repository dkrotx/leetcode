class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        
        # store product from right
        prod = 1
        res = nums[:]
        for i in reversed(range(1, len(res))):
            prod *= res[i]
            res[i] = prod
        
        # face left product (lprod) with right product
        prod = 1
        for i in range(len(res)-1):
            res[i] = prod * res[i+1]
            prod *= nums[i]
            
        res[len(res)-1] = prod
        
        return res
