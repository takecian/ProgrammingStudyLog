from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        ans = []
        for v, c in counter.items():
            if c == 1:
                ans.append(v)

        return ans
