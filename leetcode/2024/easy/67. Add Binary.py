class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ''

        remainder = 0
        for i in range(1, max(len(a), len(b))+1):
            first = 0 if i > len(a) else int(a[-i])
            second = 0 if i > len(b) else int(b[-i])
            temp = first + second + remainder

            remainder = 1 if temp > 1 else 0
            temp = 0 if temp%2 == 0 else 1

            result = str(temp) + result

        if remainder == 1:
            result = '1' + result

        return result


s = Solution()
print(s.addBinary('11', '1'))
assert s.addBinary('11', '1') == '100'


