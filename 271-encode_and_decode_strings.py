import base64

class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        res = []
        for s in strs:
            res.append(base64.b64encode(s))
            
        return ("%d:" % len(strs)) + ','.join(res)
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        res = []
        parts = s.split(':')
        n = int(parts[0])
        
        if n:
            for blk in parts[1].split(','):
                res.append(base64.b64decode(blk))
            
        return res
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
