class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        matrix = defaultdict(list)
        for i in edges:
            matrix[i[0]].append(i[1])
            matrix[i[1]].append(i[0])

        seen = set()
        ans = 0

        for i in range(0,n):

            if i not in seen: 
                queue = deque([i])
                seen.add(i)
                ans += 1

                while len(queue)>0:
                    node = queue.popleft()

                    for j in matrix[node]:
                        
                        if j not in seen:
                            queue.append(j)
                            seen.add(j)
        return ans
                        
                        






            