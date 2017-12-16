class Solution:
    @staticmethod
    def next_perm(arr):
        for i in reversed(range(len(arr)-1)):
            if arr[i] < arr[i+1]:
                next_i = i+1
                for j in range(i+2, len(arr)):
                    if arr[j] > arr[i] and arr[j] <= arr[next_i]:
                        next_i = j
                
                arr[i], arr[next_i] = arr[next_i], arr[i]
                arr[i+1:] = reversed(arr[i+1:])
                return True
        
        return False
    
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = [nums[:]]
        while self.next_perm(nums):
            res.append(nums[:])
            
        return res
