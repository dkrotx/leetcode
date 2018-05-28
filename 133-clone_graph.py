# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        self.seen = {}
        return self.deepCopy(node) if node else None
    
    def deepCopy(self, node):
        if node.label in self.seen:
            return self.seen[node.label]
        
        copy = UndirectedGraphNode(node.label)
        self.seen[node.label] = copy
        
        for n in node.neighbors:
            copy.neighbors.append(self.deepCopy(n))
            
        return copy
