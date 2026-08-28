class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        grid = [[0 for i in range(0,len(heights[j]))] for j in range(0,len(heights))]
        dx = [0,0,-1,1]
        dy = [-1,1,0,0]

        def bfs(x,y,seen):

            def isValid(x,y):
                if x>=0 and x<len(heights) and y>=0 and y<len(heights[x]):
                    return True
                return False

            nonlocal grid 
            queue = deque([(x,y)])

            if (x,y) not in seen:
                grid[x][y] += 1
                seen.add((x,y))

            while len(queue) > 0:
                x,y = queue.popleft()

                for c in range(0,len(dx)):
                    row = x + dx[c]
                    col = y + dy[c]

                    if (row,col) not in seen and isValid(row,col) and heights[row][col] >= heights[x][y]:
                        grid[row][col] += 1
                        queue.append((row,col))
                        seen.add((row,col))

        seen = set()
        for i in range(0,len(heights)):
            print((i,0))
            bfs(i,0,seen)

        for i in range(1,len(heights[0])):
            print((0,i))
            bfs(0,i,seen)

        seen = set()
        for i in range(0,len(heights)):
            print((i,len(heights[0])))
            bfs(i,len(heights[0])-1,seen)

        for i in range(0,len(heights[0])-1):
            print((len(heights),i))
            bfs(len(heights)-1,i,seen)

        ans = []
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                if grid[i][j] == 2:
                    ans.append([i,j])
        return ans


        


        

