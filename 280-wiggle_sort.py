class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        res = []
        l, h = 0, len(nums)-1
        
        while l < h:
            res.append(nums[l])
            res.append(nums[h])
            l += 1
            h -= 1
            
        if l == h:
            res.append(nums[l])
            
        for i,x in enumerate(res):
            nums[i] = x
            
# 1, 2, 3
# l,h=0,2
# 1, 3  (l=1,h=1)
