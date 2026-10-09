class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # build adjList
        N = len(points)
        adjList = defaultdict(list)
        # create adjList from every point to every other point
        for i in range(N):
            x1,y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x2-x1) + abs(y1-y2)
                adjList[i].append([dist, j])
                adjList[j].append([dist, i])
        # init visit, output, minHeap
        visited = set()
        output = 0
        minHeap = [[0,0]]
        # while len of visit nodes < number of nodes:
        while len(visited)<N:
            # minHeap pop
            dist, node = heapq.heappop(minHeap)
            # check if already present in visit, then continue
            if node in visited: continue
            # add to visited
            visited.add(node)
            # update output
            output += dist
            # for every other neighbour
            for distance, neighbour in adjList[node]:
                # heappush if minimum and not visited
                if neighbour not in visited:
                    heapq.heappush(minHeap, (distance, neighbour))

        return output