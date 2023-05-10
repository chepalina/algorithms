class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 121 = true
        # -121 = false
        # 11 = true
        # 0 = true
        # 12345 = false

        input = x

        if x < 0:
            return False

        reverse = 0

        while x != 0:
            remainder = x%10
            x //= 10
            reverse = reverse*10 + remainder

        return (input == reverse)


