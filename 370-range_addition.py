class Solution:
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        arr = [0] * length
        for start, end, diff in updates:
            arr[start] += diff
            if end+1 < length:
                arr[end+1] -= diff
        
        cur = 0
        for i in range(length):
            cur += arr[i]
            arr[i] = cur
            
        return arr
