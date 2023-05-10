from typing import List

class Solution1:
    def plusOne(self, digits: List[int]) -> List[int]:
        # [1] -> [2]
        # [1,2,3] -> [1,2,4]
        # [9] -> [1,0]
        # [1,2,9] -> [1,3,0]
        # [9,9,9] -> [1,0,0,0]

        add = 1
        index = len(digits)-1

        while add == 1 and index >= 0:
            current = digits[index] + 1

            if current < 10:
                digits[index] = current
                add = 0
            else:
                digits[index] = 0
                add = 1

            index -= 1

        if add == 1:
            digits.insert(0, 1)

        return digits


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        i = 1

        while i<=l:
            if digits[-i]!=9:
                digits[-i]+=1;
                return digits
            else:
                digits[-i]=0
                i+=1
        return [1]+digits

print( "[1] -> [2]-> actual ", Solution().plusOne([1]))
print( "[1,2,3] -> [1,2,4]-> actual ", Solution().plusOne([1,2,3]))
print( "[9] -> [1,0]-> actual ", Solution().plusOne([9]))
print( "[1,2,9] -> [1,3,0]-> actual ", Solution().plusOne([1,2,9]))
print( "[9,9,9] -> [1,0,0,0]-> actual ", Solution().plusOne([9,9,9] ))

