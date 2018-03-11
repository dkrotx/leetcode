import random

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.hash = dict()
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.arr.append(val)
        idx = len(self.arr) - 1
        
        if val in self.hash:
            self.hash[val].add(idx)
            return False
        
        self.hash[val] = set([idx])
        return True

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.hash:
            return False
        
        last_pos = len(self.arr) - 1
        if last_pos in self.hash[val]:
            self.hash[val].remove(last_pos)
        else:
            last_val = self.arr[-1]
            pos = self.hash[val].pop()
            self.arr[pos] = self.arr[last_pos]
            self.hash[last_val].remove(last_pos)
            self.hash[last_val].add(pos)
            
        self.arr.pop()
        # is there other references to val?
        if not self.hash[val]:
            del self.hash[val]
            
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.arr)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
