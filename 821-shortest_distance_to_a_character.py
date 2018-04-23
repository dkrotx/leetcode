class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        distances = []
        prev_c, next_c = -100500, S.index(C)
        for i, c in enumerate(S):
            if i > next_c:
                prev_c = next_c
                try:
                    next_c = S.index(C, i)
                except ValueError:
                    next_c = 100500
                    
            distances.append(min(i - prev_c, next_c - i))
            
        return distances
