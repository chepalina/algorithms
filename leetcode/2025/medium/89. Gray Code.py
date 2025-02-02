from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]

        prev = self.grayCode(n - 1)
        first = [e << 1 for e in prev]
        second = [(e << 1) | 1 for e in reversed(prev)]

        return first + second

    def grayCode2(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1 :
            return [0, 1]

        result = [0, 1]
        cur = 1
        for i in range(2, n+1):
            cur <<= 1
            tmp = result.copy()
            for j in range(len(tmp)-1, -1, -1):
                result.append(cur+result[j])

        return result

s = Solution()

print(s.grayCode2(3))