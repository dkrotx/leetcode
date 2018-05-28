class Vertex:
    def __init__(self):
        self.discovered = False
        self.processed = False
        self.outcomes = []

class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.verteces = [Vertex() for _ in range(numCourses)]
        
        """ run DFS and check for cycle
            If there is no cycle, it's possible
        """
        for req in prerequisites:
            dst, src = req
            self.verteces[src].outcomes.append(self.verteces[dst])
        
        for v in self.verteces:
            if not self.runDFSAndCheckCycle(v):
                return False
            
        return True
    
    def runDFSAndCheckCycle(self, v):
        v.discovered = True
        
        for u in v.outcomes:
            if u.discovered:
                if not u.processed:
                    return False
            elif not self.runDFSAndCheckCycle(u):
                return False
            
        v.processed = True
        return True
