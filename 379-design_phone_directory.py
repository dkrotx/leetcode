class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.max_nums = maxNumbers
        self.next_free = 0
        self.used_nums = set()
        self.free_nums = set()

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        if len(self.used_nums) == self.max_nums:
            return -1
            
        if self.free_nums:
            num = self.free_nums.pop()
            self.used_nums.update([num])
            return num
            
        num = self.next_free
        self.used_nums.update([num])
        self.next_free += 1
        return num

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return number >= 0 and number < self.max_nums and number not in self.used_nums

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        if number in self.used_nums:
            self.used_nums.remove(number)
            self.free_nums.update([number])
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
