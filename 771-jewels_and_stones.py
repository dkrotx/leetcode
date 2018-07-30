class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels = {c for c in J}
        cnt = 0
        for c in S:
            if c in jewels:
                cnt += 1
                
        return cnt
