class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        i = 1
        j = 0
        count = 0
        while i < len(intervals):
            while i < len(intervals) and intervals[i][0] < intervals[j][1]:
                i += 1
                count += 1
            j = i
            i += 1
        return count