class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ''.join(self.decodeSubstring(s, 0)[0])
    
    @staticmethod
    def parseNum(s, pos):
        for i in range(pos, len(s)):
            if not ('0' <= s[i] <= '9'):
                break
                
        if i > pos:
            return int(s[pos:i]), i
        return None, pos
                
        
    def decodeSubstring(self, s, pos):
        res = []
        while pos < len(s):
            repeat, pos = self.parseNum(s, pos)
            if repeat is not None:
                substr, pos = self.decodeSubstring(s, pos+1) # offset next to '['
                res.extend(repeat * substr)
            elif s[pos] == ']':
                pos += 1
                break
            else:
                res.append(s[pos])
                pos += 1
            
        return res, pos
