class Solution:

    def minDistance(self, word1: str, word2: str) -> int:

        dp = [[0]*(len(word1)+1) for _ in range(len(word2)+1)]

        for i in range(len(dp[0])):
            dp[-1][i] = len(word1) - i

        for j in range(len(dp)):
            dp[j][-1] = len(word2) - j

        for i in range(len(dp) - 2, -1, -1):
            for j in range(len(dp[0]) - 2, -1, -1):
                min_count = min(dp[i + 1][j], dp[i][j + 1 ], dp[i + 1][j + 1])

                if word2[i] != word1[j]:
                    min_count += 1

                dp[i][j] = min_count

        return dp[0][0]

s = Solution()

assert s.minDistance(word1 = "horse", word2 = "ros") == 3
assert s.minDistance(word1 = "intention", word2 = "execution") == 5
