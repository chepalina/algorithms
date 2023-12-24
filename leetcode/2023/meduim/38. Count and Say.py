class Solution:
    def countAndSay(self, n: int) -> str:

        target = "1"

        if n == 1:
            return target

        for i in range(2, n + 1):
            target = self._countAndSay(target)

        return target

    def _countAndSay(self, s: str) -> str:

        # "1" -> "11"
        # "21" - > "1211"
        # "1211" -> "111221"

        new_s = ""
        count = 0
        prev = s[0]

        for element in s:
            if element == prev:
                count += 1
            else:
                new_s += str(count) + prev
                count = 1
                prev = element

        new_s += str(count) + prev

        return new_s
