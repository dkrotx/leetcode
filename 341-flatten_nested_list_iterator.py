# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# curList = [1, [], 3]

# curPos = -1
# _find_next_value:
class NestedIterator(object):
    
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        self.cur_val = None
        self.cur_list = nestedList
        self.cur_pos = -1
        self._find_next_value()
        
    def _step_in(self, lst):
        self.stack.append((self.cur_list, self.cur_pos))
        self.cur_list = lst
        self.cur_pos = -1
        
    def _step_out(self):
        if self.stack:
            self.cur_list, self.cur_pos = self.stack.pop()
        else:
            self.cur_list = None
    
    def _find_next_value(self):
        self.cur_val = None
        
        while self.cur_val is None and self.cur_list is not None:
            self.cur_pos += 1
        
            if self.cur_pos < len(self.cur_list):
                ni = self.cur_list[self.cur_pos] # NestedInteger
                if ni.isInteger():
                    self.cur_val = ni.getInteger()
                else:
                    self._step_in(ni.getList())
            else:
                self._step_out()
        
    def next(self):
        """
        :rtype: int
        """
        val = self.cur_val
        self._find_next_value()
        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cur_val is not None
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
