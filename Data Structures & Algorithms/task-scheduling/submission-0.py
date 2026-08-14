class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [(-i,j) for j, i in count.items()]
        heapq.heapify(maxHeap)
        queue = deque()
        time = 0

        while len(maxHeap)>0 or len(queue)>0:
            time += 1 

            if not maxHeap:
                time = queue[0][2]

            else:
                item = heapq.heappop(maxHeap)
                remaining = 1 + item[0]

                if remaining != 0:
                    queue.append((item[1], remaining, time+n))

            if queue and queue[0][2] == time:
                i,j,k = queue.popleft()
                heapq.heappush(maxHeap,(j,i))

        return time




                
            
                

            





        

        return 0
