from typing import List

# Input: nums = [1]
# Output: [[1]]

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]


# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Получаем следующий результат из предыдущего
# динамика - первый случай крайний - список длины 1
# второй список получаем путем комбинации списка 1 со след числом - длина списка 1*2
# третий список - 2 (длина списка на пред шаге) * 3 = 6
# четвертый список - 6 (длина списка на пред шаге) * 4 = 24

# мат обоснование для списка из 3 (на первом месте может быть 3 числа, на втором 2, на третьем 1)
# _ _ _
# 3 2 1 -> 3*2*1 = 6

# _ _ _ _
# 4 3 2 1 -> 24


# Time: O(E+V) which is the same as => O(N*N!)


from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        target = []

        if len(nums) ==1:
            return [nums[:]]

        for _ in nums:

            n = nums.pop(0)

            perms =  self.permute(nums)

            for p in perms:
                p.append(n)

            target.extend(perms)

            nums.append(n)

        return target



class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return []

        el = nums.pop()
        target = [[el]]

        while nums:
            temp_target = []
            el = nums.pop()

            for t in target:
                for index in range(len(t)+1):
                    temp_target.append(t[0:index] + [el] + t[index:])

            target = temp_target

        return target




s = Solution()

print(s.permute([1,2,3,4]), len(s.permute([1,2,3,4])))

