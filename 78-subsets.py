class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        for n in range(len(nums)+1):
            res.extend(Solution.combinations(nums, n))
                
        return res
                
    @staticmethod
    def combinations(nums, n, i=0):
        res = []
        further = len(nums) - i - 1
        
        if further >= n:
            res = Solution.combinations(nums, n, i+1)
        
        if n > 0:
            for v in Solution.combinations(nums, n-1, i+1):
                res.append([nums[i]] + v)
            
        return res if res else [[]]
