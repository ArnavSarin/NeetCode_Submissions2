class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        matrix = defaultdict(list)
        indegrees = [0] * numCourses

        for i in prerequisites:
            a,b = i
            matrix[b].append(a)
            indegrees[a] += 1
        
        queue = deque()

        for i in range(0,len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)

        counter = 0
        ans = []

        print(queue)

        while len(queue)>0:
            course = queue.popleft()
            ans.append(course)
            counter += 1

            for i in matrix[course]:
                indegrees[i] -= 1

                if indegrees[i] == 0:
                    queue.append(i)

        if counter == numCourses:
            return ans

        return []

        
