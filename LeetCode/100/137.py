class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once = 0
        twice = 0
        for num in nums:
            once = ~twice & (once ^ num)
            twice = ~once & (twice ^ num)

        return once