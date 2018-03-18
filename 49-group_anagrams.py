from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = defaultdict(list)
        for s in strs:
            h = ''.join(sorted(s))
            groups[h].append(s)
            
        return list(groups.values())
