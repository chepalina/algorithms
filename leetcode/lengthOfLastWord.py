class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # "word" -> 4
        # "word word word word" -> 4
        # " word" -> 4
        # "word word word      word" -> 1
        # "word " -> 4
        # "word    " -> 4
        # "    word    " -> 4

        # "" -> 0
        # "     " -> 0

        word_len = 0

        for i in range(len(s) - 1, 0, -1):

            if s[i] == " " and word_len == 0:
                continue

            elif s[i] == " " and word_len != 0:
                break

            elif s[i] != " ":
                word_len += 1

        return word_len
