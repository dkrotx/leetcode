"""
Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?
"""

class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.lists = [v1, v2]
        self.frontier = -1
        self.nextFrontier()
        
    def nextFrontier(self):
        self.frontier += 1
        
        # little optimization
        for lst in self.lists:
            if len(lst) <= self.frontier:
                self.lists = list(filter(lambda x: len(x) > self.frontier, self.lists))
                break
        
        self.cur_list_id = 0

    def next(self):
        """
        :rtype: int
        """
        ret = self.lists[self.cur_list_id][self.frontier]
        
        self.cur_list_id += 1
        if self.cur_list_id == len(self.lists):
            self.nextFrontier()
            
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cur_list_id < len(self.lists)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
