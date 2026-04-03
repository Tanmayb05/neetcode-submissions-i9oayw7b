class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        min_heap = []
        for i in count.keys():
            heapq.heappush(min_heap, (count[i], i))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(min_heap)[1])
        return res
        