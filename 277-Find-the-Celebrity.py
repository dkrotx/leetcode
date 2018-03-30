# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        guests = list(range(n))
        while len(guests) >= 2:
            a = guests.pop()
            b = guests.pop()
            
            if knows(a, b):
                if not knows(b, a):
                    guests.append(b)
            else:
                if knows(b, a):
                    guests.append(a)
            
        
        """ check what celebrity doesn't know anyone """
        if guests:
            x = guests[0]
            for i in range(n):
                if x != i and knows(x, i):
                    return -1
            return x
        
        return -1
