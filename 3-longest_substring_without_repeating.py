class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        start = 0
        track = dict()
        for i, c in enumerate(s):
            if c in track:
                # to add this symbol "c" we have to remove
                # all symbols we know before and including "c"
                prev_pos = track[c]
                for _ in range(start, prev_pos+1):
                    del track[s[_]]
                start = prev_pos+1
            
            track[c] = i
            max_len = max(max_len, i - start + 1)
            
        return max_len
