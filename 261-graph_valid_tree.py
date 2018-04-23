class Node:
    def __init__(self):
        self.outcomes = []
        self.visited = False
    
class Solution:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        nodes = [Node() for i in range(n)]
        for start, end in edges:
            nodes[start].outcomes.append(nodes[end])
            nodes[end].outcomes.append(nodes[start])
            
        """ Now start from first node and mark all nodes.
            To be a proper tree these nodes have to be marked. And marked only once.
        """
        if not self.runBFS(nodes[0]):
            return False
        
        for n in nodes:
            if not n.visited:
                return False
            
        return True
        
    def runBFS(self, node, came_from = None):
        if node.visited:
            return False
        
        node.visited = True
        for n in node.outcomes:
            if n is not came_from:
                if not self.runBFS(n, node):
                    return False
                
        return True
