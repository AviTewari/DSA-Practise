class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = defaultdict(int)
        for i in range(len(tasks)):
            count[tasks[i]] += 1
        
        maxheap = [-cnt for cnt in count.values()]
        heapq.heapify(maxheap)
        time = 0
        q= deque()

        while maxheap or q:
            time+=1
            if maxheap:
                c = 1+ heapq.heappop(maxheap)
                if c:
                    q.append([c, time+n])
            if q and q[0][1] == time:
                a = q.popleft()
                heapq.heappush(maxheap, a[0])
        return time

                

