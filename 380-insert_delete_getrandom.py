import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.elems_hash = dict()
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.elems_hash:
            return False
        
        self.elems_hash[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.elems_hash:
            return False
        
        # swap element with last one if needed
        i = self.elems_hash[val]
        last_i = len(self.arr) - 1
        if i != last_i:
            self.elems_hash[self.arr[last_i]] = i
            self.arr[i] = self.arr[last_i]
        
        self.arr.pop()
        del self.elems_hash[val]
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
