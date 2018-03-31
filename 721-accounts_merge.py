class Node:
    def __init__(self, email):
        self.email = email
        self.conns = set()
        self.visited = False


class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        self.email2node = dict()
        merged = []
        
        for acc in accounts:
            self.addEmails(acc[0], acc[1:])
        
        for name, node in self.email2node.values():
            if not node.visited:
                common_emails = sorted(self.getConnectedNodes(node))
                merged.append([name] + common_emails)
                
        return merged
    
    """ get interconnected nodes, and return their emails """
    def getConnectedNodes(self, node):
        res = []
        frontier = [node]
        node.visited = True
        
        while frontier:
            next_frontier = []
            
            for node in frontier:
                res.append(node.email)
                for near in filter(lambda n: not n.visited, node.conns):
                    next_frontier.append(near)
                    near.visited = True

            frontier = next_frontier
            
        return res
    
    """ add emails of given man (name) to graph """
    def addEmails(self, name, emails):
        prev = None
        
        for e in emails:
            if e not in self.email2node:
                self.email2node[e] = (name, Node(e))
                
            node = self.email2node[e][1]
            assert(name == self.email2node[e][0])
            
            if prev:
                prev.conns.add(node)
                node.conns.add(prev)
            
            prev = node
