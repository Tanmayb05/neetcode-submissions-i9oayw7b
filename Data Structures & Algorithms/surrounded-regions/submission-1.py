class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board); COLS = len(board[0])
        
        # 1. Turn all side O's and surrounding O's to T's
        def changeT(r,c):
            if r<0 or r==ROWS or c<0 or c==COLS or board[r][c]!="O":
                return
            board[r][c] = "T"
            changeT(r+1,c)
            changeT(r-1,c)
            changeT(r,c+1)
            changeT(r,c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if (r in [0,ROWS-1] or c in [0,COLS-1]) and board[r][c]=="O":
                    changeT(r,c)

        # 2. Turn all O's to X's
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=="O":
                    board[r][c] = "X"
        # 3. Turn all T's to O's
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=="T":
                    board[r][c] = "O"
