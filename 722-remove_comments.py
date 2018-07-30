class Solution:
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        inside_multyline = False
        new_line = ''
        
        res = []
        for line in source:
            i = 0
            while i < len(line):
                two_chars = line[i:i+2]
                
                if inside_multyline:
                    if two_chars == '*/':
                        inside_multyline = False
                        i += 2
                        continue
                else:
                    if two_chars == '//':
                        break
                    if two_chars == '/*':
                        inside_multyline = True
                        i += 2
                        continue
                        
                    new_line += line[i]
                
                i += 1
                
            if new_line and not inside_multyline:
                res.append(new_line)
                new_line = ''
        
        return res
