class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zeros = 0
        pos = 0
        for i in range(n):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1

        for i in range(pos, n):
            nums[i] = 0