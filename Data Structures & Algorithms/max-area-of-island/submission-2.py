class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def validSquare(x,y):
            if x>=0 and y>=0 and x<len(grid) and y<len(grid[x]):
                return True
            return False

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        starting = []
        seen = set()
        ans = 0
        
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                if grid[i][j] == 1:
                    starting.append((i,j))
                else:
                    seen.add((i,j))

        for i in starting:
            if i not in seen:
                seen.add(i)
                row,col = i
                area = 1
                queue = deque([(row,col)])

                while len(queue)>0:
                    x,y = queue.popleft()

                    ans = max(area,ans)

                    for j in range(0,len(dx)):
                        if validSquare(x+dx[j],y+dy[j]) and (x+dx[j],y+dy[j]) not in seen:
                            area += 1
                            queue.append((x+dx[j],y+dy[j]))
                            seen.add((x+dx[j],y+dy[j]))

        return ans
                
                    
