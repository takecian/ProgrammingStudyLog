import itertools


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        sum_distance = 0
        for w in workers:
            bikes.sort(key=lambda b: -(abs(w[0] - b[0]) + abs(w[1] - b[1])))
            sum_distance += abs(w[0] - bikes[-1][0]) + abs(w[1] - bikes[-1][1])
            bikes.pop()

        return sum_distance