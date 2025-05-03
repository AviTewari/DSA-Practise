class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = defaultdict(int)
        for k,v in enumerate(tasks):
            count[k]+=1
        maxheap = [-cnt for cnt in count.values()]
        heapq.heapify(maxheap)
        q=deque()
        time = 0
        while maxheap or q:
            time += 1
            if not maxheap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxheap)
                q.append([cnt, time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])
        return time
                

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time