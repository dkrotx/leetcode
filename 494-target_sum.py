from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.cache = defaultdict(dict)
        self.nums = nums
        return self.findWays(S)

    def findWays(self, total, i=0):
        if i == len(self.nums):
            return 1 if not total else 0

        if total not in self.cache[i]:
            nways  = self.findWays(total - self.nums[i], i+1)
            nways += self.findWays(total + self.nums[i], i+1)
            self.cache[i][total] = nways

        return self.cache[i][total]
