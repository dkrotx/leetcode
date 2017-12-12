class Solution(object):
    def convert(self, s, numRows):
        # 1: 0, step 2*N-2, ...
        # o: i, step (N-i)*2, step (i-1)*2, ...
        # N: N, step 2*N-2, ...
        
        if not s:
            return ""
        if numRows == 1:
            return s
        
        res = ""
        
        # 1
        for i in range(0, len(s), 2*numRows-2):
            res += s[i]
        
        # others    
        for row in range(1, numRows-1):
            i = row
            steps = [ (numRows-(row+1))*2, row*2 ]
            step = 0
            while i < len(s):
                res += s[i]
                i += steps[step % len(steps)]
                step += 1
        # N 
        for i in range(numRows-1, len(s), 2*numRows-2):
            res += s[i]
            
        return res
