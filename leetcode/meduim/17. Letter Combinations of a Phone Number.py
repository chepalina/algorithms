from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 012 012 -> 00 01 02 10 11 12 20 21 22
        # 012345678 012 -> 00 01 ...

        digits_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        if not digits:
            return []

        target_list = [i for i in digits_map.get(digits[0])]

        for i in range(1, len(digits)):
            current = [i for i in digits_map.get(digits[i])]

            temp = []
            for t in target_list:
                for c in current:
                    temp.append(t + c)

            target_list = temp

        return target_list
