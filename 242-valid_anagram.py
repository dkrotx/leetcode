class Solution(object):
    def isAnagram(self, s, t):
        return len(s) == len(t) and sorted(s) == sorted(t)
