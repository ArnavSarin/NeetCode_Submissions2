class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def inBoard(x,y):
            if x>=0 and x<len(board) and y>=0 and y<len(board[x]):
                return True
            return False
        

        neighbors = [(-1,0),(1,0),(0,-1),(0,1)]

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]==word[0]:
                    stack = [(board[i][j],(i,j),{(i,j)})]
        # stack = [(board[0][0],(0,0),{(0,0)})]

                    while len(stack)>0:
                        node, last_node, path = stack.pop()

                        if word in node:
                            return True

                        for r, c in neighbors:
                            row = last_node[0] + r
                            col = last_node[1] + c
                            if inBoard(row,col) and (row,col) not in path:
                                    updated = path.copy()
                                    updated.add((row, col))
                                    stack.append((node + board[row][col],(row,col), updated))
        return False

            


            