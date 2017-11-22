from collections import deque

class SlidingWindowMax:
    def __init__(self, k):
        """ self.win will store pairs of {value, nrefs} """
        self.win = deque()
        self.k = k
        
    def append(self, v):
        while self.win and self.win[-1][0] < v:
            self.win.pop()
            
        if self.win and self.win[-1][0] == v:
            self.win[-1][1] += 1
        else:
            self.win.append([v, 1])
            
    def remove(self, v):
        if self.win and self.win[0][0] == v:
            self.win[0][1] -= 1
            if not self.win[0][1]:
                self.win.popleft()
                
    def getmax(self):
        return self.win[0][0]

class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        mx = SlidingWindowMax(k)
        
        if not nums or len(nums) < k:
            return []
        
        for i in range(k):
            mx.append(nums[i])
        
        res = [mx.getmax()]
        
        for i in range(k, len(nums)):
            mx.remove(nums[i-k])
            mx.append(nums[i])
            res.append(mx.getmax())
        
        return res
