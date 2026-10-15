class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if intervals is None:
            return []

        res = []

        for i, interval in enumerate(intervals):
            currStart, currEnd = interval 
            if currEnd < newInterval[0]:
                res.append(interval)            
            elif currStart > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval = [min(currStart, newInterval[0]), max(currEnd, newInterval[1])]
        res.append(newInterval)
        return res