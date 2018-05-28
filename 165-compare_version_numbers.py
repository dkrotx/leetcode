class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        def v_to_int(s):
            return list(map(int, s.split('.')))
            
        v1 = v_to_int(version1)
        v2 = v_to_int(version2)
        
        for i in range(max(len(v1), len(v2))):
            num1 = v1[i] if len(v1) > i else 0
            num2 = v2[i] if len(v2) > i else 0
            
            
            if num1 != num2:
                return 1 if num1 > num2 else -1

        return 0
