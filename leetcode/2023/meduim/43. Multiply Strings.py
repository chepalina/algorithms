class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        target = 0

        for i in range(len(num2) - 1, -1, -1):
            temp_target = 0
            temp_reminder = 0
            curr_num2 = int(num2[i])

            for j in range(len(num1) - 1, -1, -1):

                curr_num1 = int(num1[j])

                temp = curr_num1 * curr_num2 + temp_reminder

                temp_reminder, temp = temp // 10, temp % 10

                mnozitel = 10 ** (len(num1) - 1 - j)
                temp_target = temp * mnozitel + temp_target

            if temp_reminder > 0:
                temp_target += temp_reminder

            target = temp_target * 10 ** (len(num2) - 1 - i) + target

        return str(target)


s = Solution()

# assert s.multiply(num1 = "2", num2 = "3") == "6"
assert s.multiply(num1="123", num2="456") == "56088"
