class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        def isValid(x,y):
            if x>=0 and y>=0 and x<len(board) and y<len(board[x]):
                return True
            return False

        
        dx = [0,0,-1,1]
        dy = [-1,1,0,0]

        queue = deque()
        seen = set()

        for i in range(0,len(board)):
            if board[i][0] =='O':
                board[i][0]='Y'
                queue.append((i,0))
                seen.add((i,0))
            
            if board[i][len(board[0])-1]=='O':
                board[i][len(board[0])-1]='Y'
                queue.append((i,len(board[0])-1))
                seen.add((i,len(board[0])-1))

        for i in range(1,len(board[0])-1):
            if board[0][i] =='O':
                board[0][i]='Y'
                queue.append((0,i))
                seen.add((0,i))
            if board[len(board)-1][i] =='O':
                board[len(board)-1][i]='Y'
                queue.append((len(board)-1,i))
                seen.add((len(board)-1,i))
        
        while len(queue)>0:
            x,y = queue.popleft()

            for c in range(0,len(dx)):
                row = dx[c] + x
                col = dy[c] + y

                if isValid(row,col) and (row,col) not in seen and board[row][col] == 'O':
                    board[row][col] = 'Y'
                    queue.append((row,col))
                    seen.add((row,col))

        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                if board[i][j] != 'Y':
                    board[i][j] = 'X'
                else:
                    board[i][j] = 'O'
        


            
            


        





                                



