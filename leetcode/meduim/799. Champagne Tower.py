class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        prev_row = [poured] # overflow

        for row in range(1, query_row+1):

            glasses = [0] * (row + 1)

            for glass_i in range(len(prev_row)):
                extra = (prev_row[glass_i]-1)*0.5
                if extra > 0:

                    glasses[glass_i] += extra
                    glasses[glass_i + 1] += extra

            prev_row = glasses


        return min(prev_row[query_glass], 1)




s = Solution()


assert s.champagneTower(poured = 1, query_row = 1, query_glass = 1) == 0
assert s.champagneTower(poured = 2, query_row = 1, query_glass = 1) == 0.50000




