from collections import defaultdict

class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        tmap = defaultdict(int)
        for t in tasks:
            tmap[t] += 1
            
        return self.doTasks(list(tmap.values()), n)
        
    def doTasks(self, arr, n_idle):
        time = 0
        
        while any(arr):
            arr.sort(reverse=True)
            
            for i in range(n_idle+1):
                if i < len(arr) and arr[i]:
                    arr[i] -= 1
                
                time += 1
                if not any(arr): # ignore idle interval(s) at the end
                    break
            
        return time
