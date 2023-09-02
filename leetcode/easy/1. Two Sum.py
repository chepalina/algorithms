class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # nums = [2,7,11,15], target = 9 -> [0,1]
        # nums = nums = [3,3], target = 6 -> [0,1]
        # nums = nums = [-3,3], target = 0 -> [0,1]
        # nums = nums = [-3,8,20, -1, 3], target = 2 -> [3,4]
        # nums = nums = [], target = 2 -> []
        # nums = nums = [0], target = 2 -> []

        remainder_dict = {}

        for index, element in enumerate(nums):
            pair_index = remainder_dict.get(element)

            if pair_index is None:
                remainder_dict[target - element] = index
            else:
                return [pair_index, index]

        return []
