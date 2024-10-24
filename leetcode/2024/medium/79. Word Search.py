from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def backtracking(board, i:int, j:int, used, w):

            if not w:
                return True

            if board[i][j] != w[0] or (i, j) in used:
                return False

            used.add((i, j))
            temp_arg = []

            if i - 1 > -1:
                temp_arg.append((i-1, j))

            if j - 1 > -1:
                temp_arg.append((i, j-1))

            if i + 1 < len(board):
                temp_arg.append(( i + 1, j))

            if j + 1 < len(board[0]):
                temp_arg.append((i, j + 1))

            if not temp_arg:
                return False

            return any(backtracking(board, *args, used, w[1:]) for args in temp_arg)

        seen = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtracking(board, i, j, seen, word):
                    return True

        return False


s = Solution()

print(s.exist(board =[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word ="ABCCED"))
print(s.exist(board =[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word ="SEE"))
print(s.exist(board =[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word ="ABCB"))
