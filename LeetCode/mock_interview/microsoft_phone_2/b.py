class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return '0'

        nums = list(map(int, num))
        for j in range(k):
            i = 0
            while i < len(nums) - 1 and nums[i] <= nums[i + 1]:
                i += 1
            del nums[i]

        while len(nums) > 1 and nums[0] == 0:
            del nums[0]

        if len(nums) == 0:
            return '0'

        return ''.join(map(str, nums))



