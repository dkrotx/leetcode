class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]
        
        while len(res) <= num:
            for i in range(len(res)):
                res.append(1 + res[i])
                if len(res) > num:
                    break
                    
        return res
