class Solution:
    def isValid(self, s: str) -> bool:

        # '({[]})' -> True
        # '' -> True
        # '({)}' - > False

        brackets_mapping = {"}": "{", "]": "[",")": "("}

        stack = []

        for b in s:
            if b in brackets_mapping.values():
                stack.append(b)
            elif b in brackets_mapping:
                if not stack:
                    return False
                last_bracket = stack.pop()
                reverse = brackets_mapping.get(b)
                if last_bracket == reverse:
                    continue
                else:
                    return False
            else:
                raise Exception("Unknown symbol")

        return not stack



print([].pop())
