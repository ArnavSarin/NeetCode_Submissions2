class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def validSquare(x,y):
            if x>=0 and x<len(grid) and y>=0 and y<len(grid[x]):
                return True
            return False

        starting_squares = []
        seen = set()
        
        for row in range(0,len(grid)):
            for col in range(0,len(grid[row])):
                if grid[row][col] == "1":
                    starting_squares.append((row,col))
                if grid[row][col] == "0":
                    seen.add((row,col))


        dx = [0,0,-1,1]
        dy = [-1,1,0,0]
        ans = 0

        for i,j in starting_squares:
            if (i,j) not in seen:
                queue = deque([(i,j)])
                ans += 1

                while len(queue)>0:
                    row, col = queue.popleft()
                    for k in range(0,len(dx)):
                        if (row+dx[k], col+dy[k]) not in seen and validSquare(row+dx[k], col+dy[k]):
                            queue.append((row+dx[k], col+dy[k]))
                            seen.add((row+dx[k], col+dy[k]))

        return ans

                    


            

