class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        reverse = s[::-1]

        prev_number = 0
        int_number = 0

        for symbol in reverse:
            number = symbol_mapping.get(symbol)
            if number >= prev_number:
                int_number += number
            else:
                int_number -= number

            prev_number = number

        return int_number


s = Solution()

print(s.romanToInt("LVIII"))
