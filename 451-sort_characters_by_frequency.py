from collections import defaultdict

# Given a string, sort it in decreasing order based on the frequency of characters.

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        stat = defaultdict(int)
        for c in s:
			stat[c] += 1

        counts = sorted([(value, key) for key, value in stat.iteritems()], reverse=True)
        res = ''
        for num, ch in counts:
			res += ch*num

        return res
