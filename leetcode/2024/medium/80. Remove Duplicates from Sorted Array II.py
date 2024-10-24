class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        prev = None
        counter = 0

        for i in range(len(nums)):

            if nums[i] != prev:
                nums[k] = nums[i]
                k += 1
                counter = 1
                prev = nums[i]
            elif counter < 2:
                nums[k] = nums[i]
                k += 1
                counter += 1
            else:
                continue

        return k




