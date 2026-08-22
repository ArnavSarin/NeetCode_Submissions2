class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        def valid(x,y):
            if x>=0 and y>=0 and x<len(grid) and y<len(grid[x]):
                return True
            return False

        dx = [0,0,-1,1]
        dy = [-1,1,0,0]

        # seen = set()
        # for x in range(0,len(grid)):
        #     for y in range(0,len(grid[x])):
        #         if grid[x][y] == -1:
        #             seen.add((x,y))

        # tempSeen = seen


        for x in range(0,len(grid)):
            for y in range(0,len(grid[x])):
                if grid[x][y] == 0:
                    seen = {(x,y)}
                    queue = deque([(x,y,0)])

                    while len(queue)>0:
                        i,j,distance = queue.popleft()
 
                        grid[i][j] = min(grid[i][j], distance)

                        if grid[i][j] >= distance:
                             for direction in range(0,len(dx)):
                                row = dx[direction] + i
                                col = dy[direction] + j
                                
                                if (row,col) not in seen and \
                                valid(row,col) and grid[row][col] != -1 and \
                                grid[row][col] != 0: 
                                    seen.add((row,col))
                                    queue.append((row,col,distance+1))


                   




                    

