class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        l, r = 0, 1
        while l < r:
            m = (l + r) // 2
            mval = reader.get(m)
            
            if mval == 2147483647:
                r = m
            else:
                if target == mval:
                    return m
                if target > mval:
                    r = r*2
                    l = m + 1
                else:
                    r = m
                    
        return -1
