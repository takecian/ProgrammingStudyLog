class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        left_distance = None
        right_distance = None

        space = 0
        max_space = 0
        for s in seats:
            if s == 1:
                max_space = max(max_space, space)
                space = 0
            else:
                space += 1
        return max(seats.index(1), seats[::-1].index(1), (max_space + 1) // 2)
