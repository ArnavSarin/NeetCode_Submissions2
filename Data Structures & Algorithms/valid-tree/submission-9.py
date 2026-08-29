class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        matrix = defaultdict(list)
        indegrees = [0]*n

        for i in edges:
            a,b = i
            matrix[a].append(b)
            matrix[b].append(a)
        
        queue = deque([(0,[])])

        counter = 0

        while len(queue)>0:
            node, prev = queue.popleft()

            counter += 1

            for i in matrix[node]:
                print(prev[:-1])
                if i in prev[:-1]:
                    return False
                if len(prev)==0 or i != prev[-1]:
                    queue.append((i,prev + [node]))
        
        if counter != n:
            return False

        return True

        