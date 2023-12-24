from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        bit_vector = [0] * 10 ** 4

        for i in intervals:
            for element in range(i[0], i[1]):
                bit_vector[element] = 1

        target = []
        strat_interval = None
        prev = 0
        # 011100110
        for bit_index in range(len(bit_vector)):
            if bit_vector[bit_index] == prev:
                continue

            elif prev == 0:
                strat_interval = bit_index

            elif prev == 1:
                target.append([strat_interval, bit_index])
                # strat_interval = None

            prev = bit_vector[bit_index]

        return target


class SolutionCounter:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        bit_vector = [0] * 20

        for i in intervals:
            for element in range(i[0], i[1]):
                bit_vector[element] = 1

        target = []
        counter = 0
        # 011111100
        for bit_index in range(len(bit_vector)):
            print(bit_index, bit_vector[bit_index])
            if bit_vector[bit_index] == 1:
                counter += 1

            elif counter > 0:
                target.append([bit_index - counter, bit_index])
                counter = 0

        return target


s = SolutionCounter()
s.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]])
