class Solution:
    @staticmethod
    def comparator(a, b):
        return -1 if a + b < b + a else 1
        
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        if not any(nums):
            return '0' # special case to not handle [0,0,...]
        snums = sorted(map(str, nums), cmp=lambda a, b: cmp(b+a, a+b))
        return ''.join(snums)
