class Course(object):
    def __init__(self, id):
        self.id = id
        self.required_for = []
        self.visited = False
        self.labeled = False


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        self.graph = [Course(i) for i in range(numCourses)]
        for course,dep in prerequisites:
            self.graph[dep].required_for.append(course)
        
        self.dfs_step = 0
        self.topologic_order = []
        for node in self.graph:
            if not node.visited:
                if not self.dfs(node):
                    return []
        
        return list(reversed(self.topologic_order))
            
            
    def dfs(self, node):
        node.visited = True
        
        for i in node.required_for:
            req = self.graph[i]
            if req.visited:
                if not req.labeled:
                    return False # loop detected
            elif not self.dfs(req):
                return False
        
        node.labeled = True
        self.topologic_order.append(node.id)
        return True
