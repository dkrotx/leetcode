from collections import defaultdict

class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        assert(len(pid) == len(ppid))
        parent2pids = defaultdict(list)
        
        for i in range(len(ppid)):
            parent2pids[ppid[i]].append(pid[i])
            
        res = []
        frontier = [kill]
        
        while frontier:
            next_frontier = []
            for p in frontier: # add child(s) of every process we are about to kill
                if p in parent2pids:
                    next_frontier.extend(parent2pids[p])
                    
            res.extend(frontier)
            frontier = next_frontier
            
        return res
