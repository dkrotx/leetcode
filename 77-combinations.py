class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        max_vals = [n-k+i+1 for i in range(k)]
        arr = list(range(1, k+1))
        res = [arr[:]]
        
        while True:
            for i in reversed(range(k)):
                if arr[i] < max_vals[i]:
                    arr[i] += 1
                    for j in range(i+1, k):
                        arr[j] = arr[j-1]+1
                    
                    res.append(arr[:])
                    break
            else:
                break
                
        return res
