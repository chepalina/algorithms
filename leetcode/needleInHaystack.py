# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # needle, haystack
        # "a" "aaaaa" -> 0
        # "ab" "abab" -> 0
        # "ab" "ab" -> 0
        # "ab" "cd" -> -1
        # "sssssabddddd" "ab" -> 5
        # "sssab" "ab" -> 3
        # "abcabcde" "abcde" -> 3
        # "a" "ddddd" -> -1
        # "ab" "abab" -> -1
        # "ababd" "abababd" -> 2

        needle_i = haystack_lag = 0

        for haystack_i in range(len(haystack) - len(needle) + 1):

            haystack_lag = haystack_i

            while haystack[haystack_lag] == needle[needle_i]:
                haystack_lag +=1
                needle_i += 1


                if needle_i == len(needle):
                    return haystack_i

            needle_i = 0


        return -1



assert Solution().strStr("abababd", "ababd") == 2





class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # needle, haystack
        # "a" "aaaaa" -> 0
        # "ab" "abab" -> 0
        # "ab" "ab" -> 0
        # "ab" "cd" -> -1
        # "sssssabddddd" "ab" -> 5
        # "sssab" "ab" -> 3
        # "abcabcde" "abcde" -> 3
        # "a" "ddddd" -> -1
        # "ab" "abab" -> -1

        # ! некорректный для кейса
        # "ababd" "abababd" -> 2


        j = 0
        for i in range(len(haystack)):

            if j == len(needle):
                return i - len(needle)

            if haystack[i] == needle[j]:
                j += 1
            else:
                j = 0

        return -1


