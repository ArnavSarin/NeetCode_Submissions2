class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        matrix = defaultdict(list)
        indegrees = [0] * (len(edges)+1)

        for i in edges:
            matrix[i[0]].append(i[1])
            matrix[i[1]].append(i[0])
            indegrees[i[0]] += 1
            indegrees[i[1]] += 1

        queue = deque()
        for i in range(1, len(edges) + 1):
            if indegrees[i]==1:
                queue.append(i)

        while len(queue)>0:
            node = queue.popleft()
            indegrees[node]-=1

            for j in matrix[node]:
                indegrees[j]-=1
                if indegrees[j]==1:
                    queue.append(j)
        
        print(edges[::-1])
        for u,v in edges[::-1]:
            if indegrees[u] == 2 and indegrees[v] == 2:
                return [u,v]
        
        return []


        

        








        # print(matrix)
        # # seen = set()
        # for i in range(0,len(edges)):

        #     # if i not in seen:
        #     queue = deque([(i,[])])
        #         # seen.add(i)

        #     while len(queue)>0:
        #         node, prev = queue.popleft()

        #         for j in matrix[node]:
                    
        #             if prev == []:
        #                 print("GOT HERE")
        #                 queue.append((j,[node]))
        #             elif j in prev and j != prev[-1]:
        #                 print("GOT HERE 1")
        #                 return [node,j]
        #             else:
        #                 print("GOT HERE 2")
        #                 queue.append((j,prev + [node]))

        

            
