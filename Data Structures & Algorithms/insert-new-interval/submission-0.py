class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        n = len(intervals)
        left = 0; right = n-1
        target = newInterval[0]
        
        while left<=right:
            middle = left+(right-left)//2
            if intervals[middle][0] < target:
                left = middle + 1
            else:
                right = middle - 1

        intervals.insert(left, newInterval)

        res = []
        for interval in intervals:
            # end of the latest res interval < current interval start
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res