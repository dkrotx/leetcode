class Solution(object):
    def coinChange(self, coins, amount):
        max_amount = amount + 1
        A = [0] * max_amount
        for i in xrange(1, amount+1):
            min_amount = max_amount
            for coin in [c for c in coins if c <= i]:
                min_amount = min(A[i-coin]+1, min_amount)
            A[i] = min_amount

        return -1 if A[-1] == max_amount else A[-1]
