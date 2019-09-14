class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)  # min capacity
        right = sum(weights) # max capacity
        while left < right:
            mid = (left + right) // 2
            days = 1
            total = 0
            for w in weights:
                if total + w > mid:  # capacity over
                    days += 1
                    total = w
                else:
                    total += w
            if days <= D:
                right = mid
            else:
                left = mid + 1
        return left
