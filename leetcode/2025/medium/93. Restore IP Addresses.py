class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        result = []

        def rec(prefix: list, string:str, num:int , result: list):

            if num == 0 and not string:
                result.append(prefix)
                return

            if len(string) > 0:
                rec(prefix + [string[0]], string[1:], num - 1, result)

            if len(string) > 1 and string[0]!= '0':
                rec(prefix + [string[0:2]], string[2:], num - 1, result)

            if len(string) > 2 and string[0]!= '0' and int(string[0:3]) <=255:
                rec(prefix + [string[0:3]], string[3:], num - 1, result)


        rec([], s, 4, result)
        return [".".join(r) for r in result]


s = Solution()
print(s.restoreIpAddresses("25525511135"))
assert s.restoreIpAddresses("25525511135") ==["255.255.11.135", "255.255.111.35"]


assert s.restoreIpAddresses("0000") == ["0.0.0.0"]

print(s.restoreIpAddresses("101023"))
assert s.restoreIpAddresses("101023") == ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
