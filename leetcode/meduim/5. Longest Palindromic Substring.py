class Solution:
    def longestPalindrome(self, s: str) -> str:
        # "" -> ""
        # "bghjuyt" -> "b" ...
        # "ddddd" -> "ddddd"
        # "ababr" -> "aba", "bab"
        # "raba" -> "aba"
        # "gtglllgtg" -> "gtg", "lll"
        # "tyuuyt" -> "tyuuyt"

        #   b a b a d
        #(i)0 1 2 3 4 <-j
        # 0 1 0 1
        # 1.  1 0
        # 2.    1 0
        # 3.      1 0
        # 4.        1 0


        dp_item = [0] * len(s)
        dp = []

        for i in range(len(s)):
            dp_copy = dp_item.copy()
            dp.append(dp_copy)

        for i in range(len(s)):
            dp[i][i] = 1

        # проверка второго ряда (без условия по центру)
        for i in range(len(s)-1):
            dp[i][i+1] = 1 if s[i] == s [i+1] else 0


        for i in range(len(s)):
            for j in range(i+2, len(s)):
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0

        # print(dp)

        max_len = 0 if not s else 1
        max_i = 0
        max_j = 0
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i][j] == 1:
                    # print(i, j)
                    if j-i+1 > max_len:
                        max_len = j-i+1
                        max_i = i
                        max_j = j

        return s[max_i:max_j+1]


s = Solution().longestPalindrome("babad")
print(s)