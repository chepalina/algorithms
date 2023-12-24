# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
#
# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.



def intersect(arr1: list, arr2: list) -> list:

    hashmap = set(arr1)
    result = []

    for element in arr2:
        if element in hashmap:
            result.append(element)
            hashmap.remove(element)

    return result


assert intersect(arr1 = [1,2,2,1], arr2 = [2,2]) == [2]
assert intersect(arr1 = [4,9,5], arr2 = [9,4,9,8,4]) in [ [9,4], [4,9]]