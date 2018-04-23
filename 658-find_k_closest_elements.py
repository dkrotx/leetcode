class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        l, r = 0, len(arr)
        while l < r:
            m = (l + r) // 2
            if x < arr[m]:
                r = m
            else:
                l = m + 1
        
        # todo think how to rid that stage
        best = None
        for i in filter(lambda idx: 0 <= idx < len(arr), range(l-1, l+2)):
            diff = abs(arr[i] - x)
            if best is None or best[0] >= diff:
                best = (diff, i)
                
        l_iter = best[1]
        r_iter = l_iter + 1
        
        while r_iter - l_iter < k:
            if l_iter == 0:
                r_iter += 1
            elif r_iter == len(arr):
                l_iter -= 1
            else:
                if abs(arr[l_iter-1] - x) <= abs(arr[r_iter] - x):
                    l_iter -= 1
                else:
                    r_iter += 1
                    
        return [arr[i] for i in range(l_iter, r_iter)]
