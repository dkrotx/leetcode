# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        l = 1
        r = n
        while l < r:
            rev = (l + r) / 2
            if isBadVersion(rev):
                r = rev
            else:
                l = rev + 1
                
        return l
