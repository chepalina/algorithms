from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        target = []

        for row_i, row in enumerate(board):
            for column_i, column in enumerate(row):
                if board[row_i][column_i] != ".":

                    target.append(("r"+str(row_i), board[row_i][column_i]))

                    target.append(("c"+str(column_i), board[row_i][column_i]))

                    target.append(((row_i//3), (column_i//3), board[row_i][column_i]))


        print(target)
        return len(target) == len(set(target))



board = \
[["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]

s = Solution()
print(s.isValidSudoku(board))


