class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for u,v,w in times:
            adjList[u].append((v,w))

        minHeap = [(0,k)]
        output = 0
        visited = set()

        while minHeap:
            weight1, node1 = heapq.heappop(minHeap)

            if node1 in visited: continue
            visited.add(node1)
            output = weight1

            for node2, weight2 in adjList[node1]:
                if node2 not in visited:
                    heapq.heappush(minHeap, (weight2 + weight1, node2))
        
        return output if len(visited)==n else -1