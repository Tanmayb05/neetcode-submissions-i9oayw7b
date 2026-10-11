class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        coll = 0; colr = len(matrix[0])-1
        rowt = 0; rowb = len(matrix)-1

        while rowt <= rowb:
            rowm = rowt + (rowb-rowt)//2
            if target < matrix[rowm][0]:
                rowb = rowm - 1 
            elif target > matrix[rowm][colr]:
                rowt = rowm + 1
            else:
                break
        if rowt > rowb:
            return False
        
        while coll<=colr:
            colm = coll + (colr-coll)//2
            if target < matrix[rowm][colm]:
                colr = colm - 1
            elif target > matrix[rowm][colm]:
                coll = colm + 1
            else:
                return True
        return False