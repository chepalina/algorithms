from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # [1,3], [10,20] ---- [4,5]

        result = []
        new_start, new_end = newInterval
        inserted  = False
        for start, end in intervals:

            if start > new_end and not inserted:
                result.append([new_start, new_end])
                inserted  = True

            if start > new_end or end < new_start:
                result.append([start, end])

            elif end >= new_end:
                result.append([min(start, new_start), end])
                inserted  = True

            else:
                new_start, new_end = min(start, new_start), max(end, new_end)

        return result

    def insert_logic_optimization(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]

            elif intervals[i][1] < newInterval[0]:
                result.append(intervals[i])
            else:
                newInterval = [min( intervals[i][0], newInterval[0]), max( intervals[i][1], newInterval[1])]


        result.append(newInterval)

        return result








s = Solution()

print(s.insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))
print(s.insert_logic_optimization(intervals = [[1,3],[6,9]], newInterval = [2,5]))