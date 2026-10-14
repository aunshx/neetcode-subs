class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = res[-1]
            currStart, currEnd = intervals[i]

            if currStart > end:
                res.append(intervals[i])
                continue
            
            res[-1] = [min(start, currStart), max(currEnd, end)]
        
        return res

        
