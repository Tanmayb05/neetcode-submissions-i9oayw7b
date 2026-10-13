class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # column left right
        left = 0; right = len(matrix[0])-1

        while left<right:
            for i in range(right-left):
                top, bottom = left, right

                # save the topLeft
                topLeft = matrix[top][left+i]
                # move bottomLeft->$topLeft$
                matrix[top][left+i] = matrix[bottom-i][left]
                # move bottomRight->bottomLeft
                matrix[bottom-i][left] = matrix[bottom][right-i]
                # move $top$Right->$bottomRight$
                matrix[bottom][right-i] = matrix[top+i][right]
                # move topLeft->topRight
                matrix[top+i][right] = topLeft

            left+=1; right-=1
