class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for i in points:
            d = -(i[0]**2 + i[1]**2)
            heapq.heappush(max_heap, [d,i[0],i[1]])
            if len(max_heap)>k:
                heapq.heappop(max_heap)
        res = []
        while max_heap:
            d, x, y = heapq.heappop(max_heap)
            res.append([x,y])
        return res


