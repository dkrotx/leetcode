from collections import defaultdict

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        def countingDict(arr):
            d = defaultdict(int)
            for x in arr:
                d[x] += 1
            return d
            
        set1 = countingDict(nums1)
        set2 = countingDict(nums2)
        
        res = []
        for x, n in set1.items():
            nout = min(n, set2[x])
            res.extend([x] * nout)
            
        return res
