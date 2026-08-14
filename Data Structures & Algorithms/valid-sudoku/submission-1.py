class Solution:
    
    def smallBoard(self, board):
        seen = set()

        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                if board[i][j] == ".":
                    continue
                elif board[i][j] not in seen:
                    seen.add(board[i][j])
                else:
                    return False
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,len(board)):
            seen = set()
            for j in range (0,len(board[i])):
                if board[i][j] == ".":
                    continue
                elif board[i][j] not in seen:
                    seen.add(board[i][j])
                else:
                    return False

        for j in range(0,len(board[0])):
            seen = set()
            for i in range (0,len(board)):
                if board[i][j] == ".":
                    continue
                elif board[i][j] not in seen:
                    seen.add(board[i][j])
                else:
                    return False

        for item in range(0,9):
            row_start = (item//3)*3
            col_start = (item%3)*3

            curr_board = [row[col_start:col_start+3] for row in board[row_start:(row_start+3)]]
            
            if not self.smallBoard(curr_board):
                return False

        return True


            