class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # track: cols, posDiag, negDiag
        col = set(); posDiag = set(); negDiag = set()

        res = []
        board = [["."] * n for i in range(n)]

        # row by row dfs
        def dfs(r):
            # end case
            if r==n:
                # because in the output format needs to be in .... and not [".",".",".","."]
                copy = ["".join(row) for row in board]
                res.append(copy) #WHY?
                return
            
            for c in range(n):
                # Bad Case: 
                    # col in bounds, 
                    # positive diagonal exist, 
                    # negative diagonal exists
                # check the r+c and r-c logic
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue

                # Add to sets for happy Paths
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"

                # call the recursive
                dfs(r+1)

                # reset the values in col, posDiag, negDiag
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."

        dfs(0)
        return res