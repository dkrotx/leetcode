class Solution(object):
    def reverseWords(self, s):
        res = ""
        end = len(s) # end is always 1 symbol *beyond* word
        
        while end > 0:
            start = end
            while start > 0 and s[start-1] != ' ':
                start -= 1
            
            if start != end:
                if res:
                    res += " "
                res += s[start:end]
                
            end = start - 1
            
        return res
        
# "   a   "
# end = 6; start = 6
# "a" start = 0, end = 1
