"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        count = 0
        maxCount = 0
        start = []
        end = []
        for num in intervals:
            start.append(num.start)
            end.append(num.end)
        
        start.sort()
        end.sort()
        n = len(start)

        i,j=0,0

        while i < n and j < n:
            if start[i] < end[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            maxCount = max(maxCount, count)

        return maxCount

        