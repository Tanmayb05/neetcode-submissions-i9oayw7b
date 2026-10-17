class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Build maxHeap with counter and negating the positive values
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        # init time and queue [-cnt, idleTime]
        time = 0
        q = deque()


        # maxHeap exists or q exists
        while maxHeap or q:
            # increment time every loop
            time+=1

            # maxHeap doesnt exist but the queue exists condition
            if not maxHeap:
                # time = first queue element idleTime
                time = q[0][1]
            # maxHeap exists, build the queue
            else:
                # decrease the count
                cnt = 1 + heapq.heappop(maxHeap)
                # if count is not 0, then append the decreased count to the queue at the last
                if cnt:
                    q.append([cnt, time+n])
            
            # Schedule the Task: if queue exists and the first queue element idleTime is equal to the current time
            if q and q[0][1] == time:
                # insert into maxHeap
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
