class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1
        while l < r:
            x = numbers[l] + numbers[r]
            if x == target:
                return [l+1, r+1]
            # we can actually move it faster
            if x > target:
                r -= 1
            else:
                l += 1
