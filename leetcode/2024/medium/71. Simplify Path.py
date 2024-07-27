class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        stack = []

        for element in path.split('/'):
            if element in ['.', '']:
                continue
            if element == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(element)

        return '/' + '/'.join(stack)



s = Solution()
print(s.simplifyPath("/../"))
assert s.simplifyPath("/../") == '/'

