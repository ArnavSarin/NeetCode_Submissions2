class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def isValid(x,y):
            if x>=0 and x<len(grid) and y>=0 and y<len(grid[x]):
                return True
            return False

        dx = [0,0,-1,1]
        dy = [-1,1,0,0]

        queue = deque()
        seen = set()

        minimal_grid = [[0 for j in range(0,len(grid[i]))] for i in range(0,len(grid))]
        print(minimal_grid)

        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                if grid[i][j] == 0:
                    minimal_grid[i][j] = -1
                if grid[i][j] == 2:
                    seen = {(i,j)}
                    queue.append((i,j,0))
                    minimal_grid[i][j] = -1

                    while len(queue) > 0:
                        k,l, depth = queue.popleft()

                        if minimal_grid[k][l] == 0 or minimal_grid[k][l] > depth:
                            minimal_grid[k][l] = depth

                        for c in range(0,len(dx)):
                            row = k + dx[c]
                            col = l + dy[c]

                            if (row,col) not in seen and \
                            isValid(row,col) and grid[row][col] != 2 and grid[row][col] != 0:
                                queue.append((row,col,depth+1))
                                seen.add((row,col))

        minutes = 0
        print(minimal_grid)
        for i in range(0,len(minimal_grid)):
            for j in range(0,len(minimal_grid[i])):
                if minimal_grid[i][j] == 0:
                    return -1
                else:
                    minutes = max(minutes,minimal_grid[i][j])


        return minutes
                                



                        


                    



        
