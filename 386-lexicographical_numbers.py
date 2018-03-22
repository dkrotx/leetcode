class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        self.n = n
        self.res = []
        self.genNumbersFor(1, 10)
        return self.res


    def genNumbersFor(self, start, end):
        for x in range(start, end):
            if x > self.n:
                break
            self.res.append(x)
            if x * 10 <= self.n:
                self.genNumbersFor(x * 10, x*10 + 10)
