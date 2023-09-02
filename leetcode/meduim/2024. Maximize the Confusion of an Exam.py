class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        main_letter = "T"
        max_len_t = self.count_letters_1(main_letter, answerKey, k)

        main_letter = "F"
        max_len_f = self.count_letters_1(main_letter, answerKey, k)

        return max(max_len_t, max_len_f)

    def count_letters(self, main_letter, answerKey, k):
        counter = 0
        l = r = 0
        max_len = temp_len = 0

        while r < len(answerKey):
            letter = answerKey[r]

            if letter == main_letter:
                temp_len += 1
                r += 1
            elif counter < k:
                temp_len += 1
                counter += 1
                r += 1
            else:  # letter != main_letter and counter == k
                letter = answerKey[l]
                if letter != main_letter:
                    counter -= 1

                l += 1
                temp_len -= 1

            max_len = max(max_len, temp_len)

        return max_len

    def count_letters_1(self, main_letter, answerKey, k):
        counter = 0
        l = 0
        max_len = 0

        for i in range(len(answerKey)):
            if answerKey[i] != main_letter:
                counter += 1

            while counter > k:
                if answerKey[l] != main_letter:
                    counter -=1

                l += 1

            max_len = max(max_len, i - l + 1)

        return max_len



s = Solution()


assert s.maxConsecutiveAnswers(answerKey="TTFF", k=2) == 4
assert s.maxConsecutiveAnswers(answerKey="TFFT", k=1) == 3
assert s.maxConsecutiveAnswers(answerKey="TTFTTFTT", k=1) == 5
