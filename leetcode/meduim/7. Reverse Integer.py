class Solution:
    def reverse(self, x: int) -> int:
        # min -2 147 483 648  ->
        # максимальное значение 2 147 483 647
        # 2 147 483 647  7463831472

        iter = 0
        target = 0
        sign = x//abs(x)
        x = abs(x)

        while x > 0:
            if iter == 10:
                if x > 2:
                    return 0
                if x == 2 and sign ==1 and target > 147483647:
                    return 0
                if x == 2 and sign ==-1 and target > 147483648:
                    return 0


            target = target * 10 + x%10
            x = x//10
            iter += 1

        return target*sign

