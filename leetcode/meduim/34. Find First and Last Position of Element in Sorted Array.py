class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if not nums:
            return [-1, -1]

        left = 0
        right = len(nums)

        while left <= right:
            mid = (left + right)//2

            if nums[mid] >= target:
                right = mid- 1
            else:
                left = mid + 1

        if nums[left] != target:
            return [-1, -1]

        ans = [left]

        left = 0
        right = len(nums)

        while left <= right:
            mid = (left + right)//2

            if nums[mid] > target:
                right = mid- 1
            else:
                left = mid + 1

        ans.append(right)

        return ans


