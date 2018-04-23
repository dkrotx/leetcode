class Solution:
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        num = N
        while True:
            nearest = self.decrementNearest(num)
            if nearest == num:
                return num
            
            num = nearest
    
    def decrementNearest(self, N):
        num = [int(d) for d in str(N)]
        
        for i in range(len(num) - 1):
            if num[i+1] < num[i]:
                num[i] -= 1
                for rest in range(i+1, len(num)):
                    num[rest] = 9
                return int(''.join([str(x) for x in num]))
                
        return N
