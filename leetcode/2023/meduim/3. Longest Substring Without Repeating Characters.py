class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        max_length = 0

        left, rigth = 0, 0

        for i in range(len(s)):

            while s[i] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[i])
            right = i
            max_length = max(max_length, right-left+1)


        return max_length




class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "nvjkfldieo" -> 10
        # "aaaaa" -> 1
        # "anvajkfldieo" -> 9
        # "abcabcbb" -> 3
        # "abababaaacacac" -> 2
        # "adklmnartuie" -> 11

        max_len = 0

        for i in range(len(s)):

            outer_substr = s[i : len(s)]

            for j in range(len(outer_substr)):

                inner_susbstr = outer_substr[0:j]

                if len(inner_susbstr) == len(set(inner_susbstr)):
                    max_len = max(max_len, len(inner_susbstr))

        return max_len


class SolutionOptimal:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # "abcabcbb" -> 3

        max_len = 0
        substr = ""

        for i in range(len(s)):
            element = s[i]
            if element not in substr:
                substr += s[i]
            else:
                duplicate_index = substr.index(s[i])
                substr = substr[duplicate_index + 1 :] + s[i]

            # print(substr)

            max_len = max(max_len, len(substr))

        return max_len


class SolutionNew:
    def lengthOfLongestSubstring(self, s: str) -> int:

        substr = ""
        max_len = 0

        for i in s:
            if i not in substr:
                substr = substr + i
            else:
                index = substr.find(i)
                substr = substr[index + 1 :] + i

            max_len = max(max_len, len(substr))

        return max_len


s = SolutionNew()
print("abcabcbb -> 3, actual ->", s.lengthOfLongestSubstring("abcabcbb"))
print("nvjkfldieo -> 10, actual ->", s.lengthOfLongestSubstring("nvjkfldieo"))
print("adklmnartuie -> 11, actual ->", s.lengthOfLongestSubstring("adklmnartuie"))
print(" -> 0, actual ->", s.lengthOfLongestSubstring(""))
