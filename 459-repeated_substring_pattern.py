class Solution(object):
    def repeatedSubstringPattern(self, str):
        for n in range(1, len(str)/2+1):
            if len(str) % n != 0:
                continue
            
            substr = str[0:n]
            for i in range(n, len(str)-n+1, n):
                if str[i:i+n] != substr:
                    break
            else:
                return True
        
        return False
# abac
# ab: 2, 2, 2
