from collections import defaultdict, namedtuple

Record = namedtuple('Record', ['fn', 'type', 'timestamp'])

class FuncInfo:
    def __init__(self, fn, start):
        self.fn = fn
        self.last_start = start

class Solution:
    @staticmethod
    def parseRecord(s):
        fields = s.split(':')
        return Record(int(fields[0]), fields[1], int(fields[2]))
    
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        times = defaultdict(int)
        stack = []
        for s in logs:
            rec = Solution.parseRecord(s)
            if rec.type == 'start':
                if stack:
                    times[stack[-1].fn] += rec.timestamp - stack[-1].last_start
                stack.append(FuncInfo(rec.fn, rec.timestamp))
            else:
                assert(rec.fn == stack[-1].fn)
                times[rec.fn] += rec.timestamp - stack[-1].last_start + 1
                stack.pop()
                if stack:
                    stack[-1].last_start = rec.timestamp + 1
                    
        return list(map(lambda x: x[1], sorted(times.items())))
