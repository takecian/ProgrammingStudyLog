class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        p = 1
        for i in range(len(nums)):
            output.append(p)
            p *= nums[i]
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] = output[i] * p
            p *= nums[i]
        return output