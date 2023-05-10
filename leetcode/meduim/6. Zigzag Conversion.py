class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # "ABC" 1 -> "ABC"
        # "ABCDEF" 2 -> "ACEBDF"
        # A C E
        # B D F

        meta_list = []

        n = numRows-2

        start = 0
        

        while start < len(s):
            end = start + numRows
            if end >= len(s):
                end = len(s)

            meta_list.append(s[start:end])

            for i in range(1, n+1):
                if end >= len(s):
                    break
                position = numRows - i
                zigzag_s = (" "*(position - 1)) + s[end: end+1] + (" "*(numRows-position))
                meta_list.append(zigzag_s)
                end += 1

            start = start + numRows + ((numRows-2) if numRows > 2 else 0)

        # print(meta_list)


        target = ""
        for i in range(numRows):
            for l in meta_list:
                if len(l)>i and l[i] != " ":
                   target += l[i]

        return target 

s = Solution()
assert s.convert("PAYPALISHIRING", 3)=="PAHNAPLSIIGYIR"
assert s.convert("PAYPALISHIRING", 4)=="PINALSIGYAHRPI"

assert s.convert("A", 1)=="A"


print(s.convert("PAYPALISHIRING", 3))



