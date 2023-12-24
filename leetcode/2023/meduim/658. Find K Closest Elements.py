class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        l,r = 0, len(arr)-k

        while l!=r:
            m = (l+r)//2
            # window [m:m+k]
            first = arr[m]
            out = arr[m+k]

            if abs(first-out) < abs(out-first) or abs(first-out) == abs(out-first):
                r = m
            else:
                l = m


        return arr[m: m+k]
