class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # [2 1]
        # [1]

        if not nums:
            return -1

        rotated = True if nums[0] > nums[-1] else False

        if rotated:
            left_r = 0
            right_r = len(nums)

            while left_r <= right_r:
                middle = (right_r + left_r)//2

                # если случайно попали в нужный элемент
                if nums[middle] == target:
                    return middle

                if nums[middle] > nums[0]:
                    left_r = middle + 1
                else:
                    right_r = middle - 1

            if target > nums[-1]:
                left = 0
                right = right_r
            else:
                left = right_r +1
                right = len(nums)
        else:
            left = 0
            right = len(nums)

        while left <= right:
            middle = (right + left)//2

            if nums[middle] == target:
                return middle

            if nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        return -1






