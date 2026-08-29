class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        matrix1 = defaultdict(list)
        indegrees = [0] * numCourses

        for courses in prerequisites:
            matrix1[courses[1]].append(courses[0])
            indegrees[courses[0]] += 1

        queue = deque()

        for i in range(0,len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)

        counter = 0

        while len(queue)>0:
            course = queue.popleft()
            counter += 1

            if numCourses == counter:
                return True

            for i in matrix1[course]:
                indegrees[i] -= 1

                if indegrees[i] == 0:
                    queue.append(i)

        return False

        

        # while len(dep)>0 and len(queue)>0:

            # if coursesTaken == numCourses:
            #     return True

            # if len(queue)==0 and dep[0][0] != 0:
            #     return False

            # if len(queue)==0 
            #     while dep[0][0] == 0:
            #         queue.append(dep[0][1])
            #         heapq.heappop(dep)
            # else:
            #     value = queue.popleft()

            #     coursesTaken += 1

            #     #ONCE YOUVE REMOVED FROM THE QUEUE 
            #     #FIND ALL TASKS THAT ARE DEPENDENT ON IT VIA HASHMAP
            #     #DROP THEIR NUMBER IN THE HEAP BY 1

            #     for i in matrix1[value]:
