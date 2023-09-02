class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}

        sign_counter = 1
        target = ""

        while num > 0:
            reminder = num % 10
            num = num // 10

            round_ = reminder * sign_counter + sign_counter
            round_symbol = symbols.get(round_)

            counter_symbol = symbols.get(sign_counter)

            if round_symbol:
                target = counter_symbol + round_symbol + target
            elif reminder - 5 >= 0:
                additional_symbol = symbols.get(5 * sign_counter)
                target = additional_symbol + counter_symbol * (reminder - 5) + target
            else:
                target = counter_symbol * reminder + target

            sign_counter = sign_counter * 10

        return target
