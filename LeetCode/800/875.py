class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            speed = (left + right) // 2
            hour = 0
            for pile in piles:
                hour += pile // speed
                hour += 1 if pile % speed != 0 else 0
            if hour <= H:
                right = speed
            else:
                left = speed + 1
        return left
