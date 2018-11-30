from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = defaultdict(int)
        for x in nums:
            count[x] += 1
            
        stat = []
        for x, freq in count.items():
            stat.append((-freq, x))
            
        heapq.heapify(stat)
        res = []
        while len(res) < k:
            res.append(heapq.heappop(stat)[1])
            
        return res
