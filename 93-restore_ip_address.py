class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.ips = []
        self.restoreChunk(s)
        return self.ips
    
    @staticmethod
    def chunks2str(ip):
        return '%s.%s.%s.%s' % tuple(ip)
    
    @staticmethod
    def isValidChunk(chunk):
        return 0 <= int(chunk) <= 255 and str(int(chunk)) == chunk # 000, 010, etc are not valid strings for chunks
        
    def restoreChunk(self, s, variant = []):
        if not s:
            return
        
        if len(variant) == 3:
            if self.isValidChunk(s):
                self.ips.append(Solution.chunks2str(variant + [s]))
            return
        
        for n in range(1, min(4, len(s)+1)):
            part = s[:n]
            if self.isValidChunk(part):
                self.restoreChunk(s[n:], variant + [part])
