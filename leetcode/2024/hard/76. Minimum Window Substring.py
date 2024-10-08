class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = {}
        counter = len(t)
        l = 0
        window = (0, 10 ^ 5)

        for e in t:
            count = t_map.get(e, 0)
            t_map[e] = count + 1

        for r in range(len(s)):
            if counter > 0:
                # print("r= " + s[l : r + 1])

                cur = t_map.get(s[r], 0)

                if cur > 0:
                    counter -= 1

                t_map[s[r]] = cur - 1

            while counter == 0:
                # print("l=" + s[l : r + 1])
                if window[1] - window[0] > r - l:
                    window = (l, r)

                cur = t_map.get(s[l]) + 1
                if cur > 0:
                    counter += 1

                t_map[s[l]] = cur
                l += 1

        return "" if window == (0, 10 ^ 5) else s[window[0] : window[1] + 1]


s = Solution()

# print(s.minWindow(s="ADOBECODEBANC", t="ABC"))
assert s.minWindow(s="ADOBECODEBANC", t="ABC") == "BANC"
assert s.minWindow(s = "a", t = "a") == "a"
assert s.minWindow(s = "a", t = "aa") == ""
