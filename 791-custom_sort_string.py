class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        poses = dict()
        for pos, c in enumerate(S):
            poses[c] = pos
        
        return ''.join(sorted(T, key=lambda c: poses[c] if c in poses else ord(c)+26))
