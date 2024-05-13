class Solution:
    def breakPalindrome(self, palindrome: str) -> str:

        # a b c c b a
        # 1 2 3 3 2 1

        if len(palindrome) <= 1:
            return ""

        middle = len(palindrome) // 2

        for i in range(middle + 1):
            if palindrome[i] != "a":

                return  palindrome[0:i] + "a" + palindrome[i+1:]

        return palindrome[0:-1] + "b"




s = Solution()

assert s.breakPalindrome("abccba") == "aaccba"
assert s.breakPalindrome("a") == ""
assert s.breakPalindrome("aa") == "ab"
assert s.breakPalindrome("aaa") == "aab"
assert s.breakPalindrome("aea") == "aaa"
